from pydantic import BaseModel


class ImproveContentRequest(BaseModel):
    email_content: str
    receiver_email: str