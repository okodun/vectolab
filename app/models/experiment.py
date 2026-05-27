from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Experiment(Base):
    __tablename__ = "experiments"

    name: Mapped[str] = mapped_column(String, primary_key=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    rollout_percent: Mapped[float] = mapped_column(Float, default=50.0)


class Override(Base):
    __tablename__ = "overrides"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    experiment: Mapped[str] = mapped_column(String, primary_key=True)
    variant: Mapped[str] = mapped_column(String)
