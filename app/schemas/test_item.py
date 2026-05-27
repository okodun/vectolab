from pydantic import BaseModel, ConfigDict, Field


class TestItem(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, from_attributes=True)

    id: int = Field(gt=0, le=9_223_372_036_854_775_807)
    name: str = Field(min_length=1, max_length=100)
