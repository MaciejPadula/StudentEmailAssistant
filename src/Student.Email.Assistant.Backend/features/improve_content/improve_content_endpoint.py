from fastapi import APIRouter
from features.improve_content.request import ImproveContentRequest

router = APIRouter()

@router.post("/api/improve-content")
async def improve_content(request: ImproveContentRequest) -> str:
    return request.email_content