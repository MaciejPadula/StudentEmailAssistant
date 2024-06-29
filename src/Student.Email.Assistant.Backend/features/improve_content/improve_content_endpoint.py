from fastapi import APIRouter
from features.improve_content.request import ImproveContentRequest
import infrastructure.openai_client
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

@router.post("/api/improve-content")
async def improve_content(request: ImproveContentRequest) -> str:
    prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": """Please review and correct the content of the email provided by the user.
                    The email is written in an academic environment, so ensure that the language is formal, polite, and clear.
                    Make necessary corrections for grammar, spelling, and punctuation, and improve the overall flow and clarity of the text.
                    Respond in the language the email was written in, only with the corrected content"""
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
    return response.choices[0].message.content.strip()

