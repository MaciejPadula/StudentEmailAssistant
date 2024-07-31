from fastapi import APIRouter
from features.improve_content.request import ImproveContentRequest
import infrastructure.openai_client
from dotenv import load_dotenv
from langchain.docstore.document import Document
import json
from infrastructure.openai_client import call_lang_chain


load_dotenv()
router = APIRouter()

with open("workers_data.json", "r", encoding="utf8") as f:
    lecturers = json.load(f)

documents = [
    Document(page_content=json.dumps(x), metadata={"source": "Wikipedia"}) for x in lecturers
]

@router.post("/api/improve-content")
async def improve_content(request: ImproveContentRequest) -> str:
    prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": """Please extract name of the lecturer from the email content provided by the user. Return it in JSON format:
                    {
                      "name": "Name Surname"
                    }
                    """
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": request.email_content
                }
            ]
        }
    ]

    response = infrastructure.openai_client.call_openai_api(prompt)
    name_and_surname = json.loads(response.choices[0].message.content.strip().replace("json", "").replace("```", ""))['name']

    res = call_lang_chain(f"Jaki tytuł ma {name_and_surname}?", documents)

    prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": """
                    
                    Please review and correct the content of the email provided by the user. Try to insert lecturers's titles.
                    The email is written in an academic environment, so ensure that the language is formal, polite, and clear.
                    Make necessary corrections for grammar, spelling, and punctuation, and improve the overall flow and clarity of the text.
                    Respond in the language the email was written in, only with the corrected content.
                    
                    Allowed forms of titles are!!!:
                    - Panie Doktorze
                    - Pani Doktor
                    - Panie Profesorze
                    - Pani Profesor
                    
                    If lecturer's title is not greater or equal to dr, pealse leave the title empty!!!

                    """
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Email: {request.email_content}"
                },
                {
                    "type": "text",
                    "text": f"Title: {res['answer']}"
                }
            ]
        }
    ]

    response = infrastructure.openai_client.call_openai_api(prompt)

    return response.choices[0].message.content.strip()

