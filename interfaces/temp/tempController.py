from fastapi import APIRouter
from schemas.apiResponse import DataResponse, ListResponse, ErrorResponse, BaseResponse

router = APIRouter()

@router.get("/")
def temp():
    return DataResponse(data="temp Test",message="Temp Test")