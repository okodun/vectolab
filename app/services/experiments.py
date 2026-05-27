import hashlib

from app.repositories import experiments as experiment_repository
from sqlalchemy.orm import Session


def get_bucket(user_id: int, experiment: str) -> int:
    key = f"{user_id}:{experiment}".encode()
    hash_val = int(hashlib.sha256(key).hexdigest()[:8], 16)
    return hash_val % 100


def resolve_group(db: Session, user_id: int, experiment: str) -> str | None:
    override = experiment_repository.get_override(db, user_id=user_id, experiment=experiment)
    if override:
        return override.variant

    exp = experiment_repository.get_experiment(db, name=experiment)
    if not exp or not exp.enabled:
        return None

    if get_bucket(user_id, experiment) < exp.rollout_percent:
        return "B"

    return "A"
