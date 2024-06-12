from fastapi import APIRouter
from features.generate_title.request import GenerateTitleRequest
import infrastructure.openai_client

router = APIRouter()

@router.post("/api/generate-title")
async def generate_title(request: GenerateTitleRequest) -> str:
    prompt = f"Please generate an email title for this email:{request.email.content}.
                Email is written in an academic enviroment so be sure to use appropriate titles.
                Be polite and make sure that title is as informative as possible.
                Respond in language email was written in, only with the title."
    response = infrastructure.openai_client.call_openai_api(prompt)
    return response.choices[0].message.constent.strip()