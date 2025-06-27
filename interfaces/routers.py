from fastapi import APIRouter
from interfaces.temp import tempController
from interfaces.memo import memo_controller

api_router = APIRouter()
api_router.include_router(tempController.router, prefix="/temp", tags=["Temp Endpoint"])
api_router.include_router(memo_controller.router, prefix="/memo", tags=["Memo Endpoint"])

