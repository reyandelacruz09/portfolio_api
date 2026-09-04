import json

from sqlalchemy.orm import Session

from app.models.content import PortfolioContent


class ContentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> dict:
        rows = self.db.query(PortfolioContent).all()
        data = {}
        for row in rows:
            data[row.key] = json.loads(row.value)
        return data

    def get_by_key(self, key: str):
        return (
            self.db.query(PortfolioContent)
            .filter(PortfolioContent.key == key)
            .first()
        )

    def upsert(self, updates: dict) -> dict:
        for key, value in updates.items():
            row = self.get_by_key(key)
            if row:
                row.value = json.dumps(value)
            else:
                self.db.add(PortfolioContent(key=key, value=json.dumps(value)))
        self.db.commit()
        return self.get_all()
