from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Testing(Base):
    __tablename__ = "testing"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
