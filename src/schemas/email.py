from pydantic import BaseModel


class SendMessage(BaseModel):
    email: str
    message: str