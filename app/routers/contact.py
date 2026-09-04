from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.contact import ContactMessage, ContactResponse
from app.services.contact_service import ContactService

router = APIRouter()


@router.post("/", response_model=ContactResponse)
async def send_contact_message(contact: ContactMessage, db: Session = Depends(get_db)):
    result = ContactService(db).send_contact_message(
        name=contact.name,
        email=contact.email,
        subject=contact.subject,
        message=contact.message,
    )
    return ContactResponse(**result)
