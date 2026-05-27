from pydantic import BaseModel


class SessionState(BaseModel):
    sessionID: str
    timestamp: int
    session_length: int
