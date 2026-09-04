from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class PortfolioContent(Base):
    __tablename__ = "portfolio_content"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, nullable=False, index=True)
    value = Column(Text, nullable=False)
