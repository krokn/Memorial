from pydantic import BaseModel


class postSchemaToAdd(BaseModel):
    title: str
    content: str
    linkToPhoto: str
    x: float
    y: float