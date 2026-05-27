from contextlib import asynccontextmanager
from app.routes import experiments, test_items
from app.core.config import settings
from app.core.logging import configure_logging
from app.core.middleware import security_headers
from app.db import database
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

logger = configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create_db()
    logger.info("Database initialized.")
    yield
    logger.info("Cleaning up database resources.")


app = FastAPI(
    lifespan=lifespan,
    docs_url=None if settings.is_production else "/docs",
    redoc_url=None if settings.is_production else "/redoc",
    openapi_url=None if settings.is_production else "/openapi.json",
)

app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.allowed_hosts)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=settings.allow_credentials,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID", "X-API-Key"],
)
app.middleware("http")(security_headers)

app.include_router(experiments.router)
app.include_router(test_items.router)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(
        "Unhandled exception while processing request",
        extra={
            "request_id": getattr(request.state, "request_id", None),
            "path": request.url.path,
            "method": request.method,
        },
    )

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
        headers={"X-Request-ID": getattr(request.state, "request_id", "")},
    )


@app.get("/")
async def index():
    return {"details": "i'm up and running"}
