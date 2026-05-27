from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.authorization import authorize_roblox
from app.db.database import get_db
from app.repositories import test_items as test_item_repository
from app.schemas.test_item import TestItem

router = APIRouter(tags=["test-items"])


@router.post("/send-json", response_model=TestItem)
async def receive_json(test_item: TestItem, db: Session = Depends(get_db), _: None = Depends(authorize_roblox)):
    return test_item_repository.create_item(db=db, item=test_item)
