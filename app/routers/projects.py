from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.project import Project
from app.services.project_service import ProjectService

router = APIRouter()


@router.get("/", response_model=list[Project])
async def get_projects(db: Session = Depends(get_db)):
    return ProjectService(db).list_projects()


@router.get("/{project_id}", response_model=Optional[Project])
async def get_project(project_id: int, db: Session = Depends(get_db)):
    return ProjectService(db).get_project(project_id)
