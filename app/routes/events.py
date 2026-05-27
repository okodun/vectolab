from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.authorization import authorize_roblox
from app.db.database import get_db
from app.schemas.event import SessionState

router = APIRouter(prefix="/event", tags=["events"])


@router.post("/goh", status_code=status.HTTP_204_NO_CONTENT)
async def collect_session_data(
        payload: SessionState,
        db: Session = Depends(get_db),
        _: None = Depends(authorize_roblox)
):
    pass
