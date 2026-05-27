from app.db.database import get_db
from app.repositories import experiments as experiment_repository
from app.schemas.experiment import Experiment, GroupAssignment, GroupAssignmentRequest
from app.services import experiments as experiment_service
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.authorization import authorize_roblox

router = APIRouter(prefix="/experiment", tags=["experiments"])


@router.post("/assignment", response_model=GroupAssignment)
async def get_group_assignment(
        payload: GroupAssignmentRequest,
        db: Session = Depends(get_db),
        _: None = Depends(authorize_roblox),
):
    group = experiment_service.resolve_group(
        db=db,
        user_id=payload.user_id,
        experiment=payload.experiment,
    )

    if group is None:
        raise HTTPException(status_code=404, detail="Experiment does not exist.")

    return GroupAssignment(group=group)


@router.post("", response_model=Experiment)
async def register_experiment(exp: Experiment, db: Session = Depends(get_db), _: None = Depends(authorize_roblox)):
    existing = experiment_repository.get_experiment(db=db, name=exp.name)

    if existing:
        raise HTTPException(status_code=409, detail="Experiment already exists.")

    return experiment_repository.create_experiment(db=db, exp=exp)
