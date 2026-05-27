from pydantic import BaseModel, ConfigDict, Field


class SessionState(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    sessionID: str = Field(min_length=1, max_length=128, pattern=r"^[A-Za-z0-9_.:-]+$")
    timestamp: int = Field(strict=True, ge=0, le=9_999_999_999_999)
    session_length: int = Field(strict=True, ge=0, le=86_400)
