from fastapi import APIRouter
from features.generate_title.request import GenerateTitleRequest

router = APIRouter()

@router.post("/api/generate-title")
async def generate_title(request: GenerateTitleRequest) -> str:
    return request.email_content