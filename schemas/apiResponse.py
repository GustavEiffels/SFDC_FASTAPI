from typing import Generic,TypeVar,Optional,List,Dict,Any
from pydantic import BaseModel, Field

T = TypeVar("T")

class BaseResponse(BaseModel):
    status: str = Field("SUCCESS",description="요청 처리 상태 (success/error)")
    message: Optional[str] = Field(None, description="응답 메시지 (성공 또는 오류 메시지)")

class DataResponse(BaseResponse, Generic[T]):
    data: Optional[T] = Field(None, description="반환되는 실제 데이터 객체")

class ListResponse(BaseResponse, Generic[T]):
    data: List[T] = Field([], description="반환되는 실제 데이터 리스트")
    total_count: int = Field(0, description="리스트의 전체 항목 수 (페이지네이션 등에 사용)")

class ErrorResponse(BaseResponse):
    status: str = "error"
    code: str
    message: Optional[str] = None
    detail: Optional[Any] = None