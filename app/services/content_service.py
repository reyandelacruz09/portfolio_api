from typing import Optional

from fastapi import HTTPException, status

from app.core.security import decode_token
from app.repositories.content_repository import ContentRepository


class ContentService:
    def __init__(self, db):
        self.content_repo = ContentRepository(db)

    def get_content(self) -> dict:
        return self.content_repo.get_all()

    def update_content(self, updates: dict) -> dict:
        return self.content_repo.upsert(updates)

    @staticmethod
    def is_authorized(authorization: Optional[str]) -> bool:
        if authorization is None or not authorization.startswith("Bearer "):
            return False
        token = authorization.split(" ", 1)[1]
        return decode_token(token) is not None

    def require_admin(self, authorization: Optional[str]):
        if not self.is_authorized(authorization):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
            )
        return authorization
