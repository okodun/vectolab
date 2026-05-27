import secrets

from fastapi import Header, HTTPException

from app.core.config import settings


def authorize_roblox(x_api_key: str | None = Header(default=None, alias="X-API-Key")):
    if not x_api_key or not secrets.compare_digest(x_api_key, settings.roblox_api_secret):
        raise HTTPException(status_code=401, detail="Unauthorized")
