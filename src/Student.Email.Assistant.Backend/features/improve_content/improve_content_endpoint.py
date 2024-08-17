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
    res = call_lang_chain(f"Jaki tytuł ma {request.receiver_email}?", documents)
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

                    If the message is about a lesson or some kind of activity, use only information provided, do not assume the type of lessons or activities.

                    If an acronym is encountered, please do not try to explain what it means, simply repeat it.
                    Be sure to repeat encountered acronyms, so the information is not lost.

                    Assume sex of the receiver based on their name (receiver's name is male's name sex is MALE otherwise FEMALE).

                    Do not mix genders of the receivers.

                    Please write one greeting only (example: Szanowna Pani Doktor or Szanowny Panie Doktorze
                    not Szanowna Pani Doktor/Szanowny Panie Doktorze).

                    Titles are provided in user prompt (under "Title:"), if section is empty there are no titles.
                    It is crucial that correct titles are used.
                    
                    If lecturer's title is only mgr or only mgr inz or only inz pealse leave the title empty!!!

                    If title is equal or greater than dr, do not use lower titles.

                    Please do not alter the signature just copy and paste it, it's crucial for the app to work as intended.

                    Do not use diminutives like (e.g. poprawka).
                    
                    Result should be a HTML string containing tags for example <br/> instead of '\n' etc. It should not not be embedded in any sort of formatting block like ```
                    
                    Do not write '''html at the beggining.

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

    response = infrastructure.openai_client.call_openai_api(prompt, max_tokens=4000)
    return response.choices[0].message.content.strip()

