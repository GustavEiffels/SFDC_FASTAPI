from fastapi import FastAPI, Request
from core.config import settings
from interfaces.routers import api_router
from exceptions.handlers import add_exception_handlers
from core.logging_config import log_setup

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json"
)

# Add Exception Handler
add_exception_handlers(app)

# Add Router
app.include_router(api_router, prefix=settings.API_STR)

# Logging
logger = log_setup()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming Request: {request.method} {request.url.path}")

    response = await call_next(request)

    logger.info(f"Outgoing Response: {response.status_code} for {request.method} {request.url.path}")
    return response

@app.on_event("startup")
async def startup_event():
    logger.info("FastAPI application is starting up.")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("FastAPI application is shutting down.")