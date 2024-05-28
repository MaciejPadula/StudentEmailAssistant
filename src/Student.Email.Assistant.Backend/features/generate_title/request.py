from pydantic import BaseModel


class GenerateTitleRequest(BaseModel):
    email_content: str