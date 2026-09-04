from pydantic import BaseModel


class ContentUpdateRequest(BaseModel):
    updates: dict
