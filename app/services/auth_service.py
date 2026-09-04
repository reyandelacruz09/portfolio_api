from fastapi import HTTPException, status

from app.core.security import verify_password, create_access_token, decode_token
from app.repositories.admin_repository import AdminRepository


class AuthService:
    def __init__(self, db):
        self.admin_repo = AdminRepository(db)

    def login(self, username: str, password: str) -> dict:
        admin = self.admin_repo.get_by_username(username)
        if not admin or not verify_password(password, admin.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )
        token = create_access_token(subject=admin.username)
        return {"access_token": token, "token_type": "bearer"}

    def get_current_user(self, authorization):
        if authorization is None or not authorization.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing token",
            )
        token = authorization.split(" ", 1)[1]
        username = decode_token(token)
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )
        admin = self.admin_repo.get_by_token_subject(username)
        if not admin:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )
        return {"id": admin.id, "username": admin.username}
