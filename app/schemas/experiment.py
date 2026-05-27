from pydantic import BaseModel, ConfigDict, Field


class Experiment(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, from_attributes=True)

    name: str = Field(min_length=1, max_length=64, pattern=r"^[A-Za-z0-9_.:-]+$")
    enabled: bool
    rollout_percent: float | None = Field(default=None, ge=0, le=100)

class GroupAssignmentRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    user_id: int = Field(gt=0, le=9_223_372_036_854_775_807)
    experiment: str = Field(min_length=1, max_length=64, pattern=r"^[A-Za-z0-9_.:-]+$")

class GroupAssignment(BaseModel):
    group: str = Field(pattern=r"^[A-Za-z0-9_.:-]+$")
