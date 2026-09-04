from typing import Optional

from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse, UserOut
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    result = AuthService(db).login(data.username, data.password)
    return TokenResponse(**result)


@router.get("/me", response_model=UserOut)
def get_me(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    return AuthService(db).get_current_user(authorization)
