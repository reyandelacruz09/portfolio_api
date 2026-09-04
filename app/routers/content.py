from typing import Optional

from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.content import ContentUpdateRequest
from app.services.content_service import ContentService

router = APIRouter()


def require_admin(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    return ContentService(db).require_admin(authorization)


@router.get("/")
def get_content(db: Session = Depends(get_db)):
    return ContentService(db).get_content()


@router.put("/")
def update_content(
    request: ContentUpdateRequest,
    authorization: Optional[str] = Depends(require_admin),
    db: Session = Depends(get_db),
):
    return ContentService(db).update_content(request.updates)
