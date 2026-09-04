from app.repositories.content_repository import ContentRepository


class ContactService:
    def __init__(self, db):
        self.content_repo = ContentRepository(db)

    def send_contact_message(self, name: str, email: str, subject: str, message: str) -> dict:
        # Placeholder for future email/database storage of contact messages.
        return {"success": True, "message": "Message sent successfully"}
