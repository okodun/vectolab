from sqlalchemy.orm import Session

from app.models.test_item import Testing
from app.schemas.test_item import TestItem


def create_item(db: Session, item: TestItem) -> Testing:
    test_item = Testing(id=item.id, name=item.name)
    db.add(test_item)
    db.commit()
    db.refresh(test_item)
    return test_item
