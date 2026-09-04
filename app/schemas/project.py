from typing import List, Optional

from pydantic import BaseModel


class Project(BaseModel):
    id: int
    title: str
    description: str
    image_url: Optional[str] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    technologies: List[str] = []
