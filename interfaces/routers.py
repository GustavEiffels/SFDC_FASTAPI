from fastapi import APIRouter
from interfaces.temp import tempController

api_router = APIRouter()
api_router.include_router(tempController.router, prefix="/temp", tags=["Temp Endpoint"])