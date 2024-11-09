from pydantic import BaseModel


class postSchemaToAdd(BaseModel):
    title: str
    content: str
    linkToPhoto: str
    address: str
    x: float
    y: float