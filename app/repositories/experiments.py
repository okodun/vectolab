from sqlalchemy.orm import Session

from app.models.experiment import Experiment, Override
from app.schemas.experiment import Experiment as ExperimentSchema


def get_experiment(db: Session, name: str) -> Experiment | None:
    return db.query(Experiment).filter_by(name=name).first()


def get_override(db: Session, user_id: int, experiment: str) -> Override | None:
    return db.query(Override).filter_by(user_id=user_id, experiment=experiment).first()


def create_experiment(db: Session, exp: ExperimentSchema) -> Experiment:
    rollout_percent = 50 if exp.rollout_percent is None else exp.rollout_percent
    db_exp = Experiment(name=exp.name, enabled=exp.enabled, rollout_percent=rollout_percent)
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp
