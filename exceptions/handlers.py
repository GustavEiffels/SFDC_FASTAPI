from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from typing import Generic,TypeVar,Optional,List,Dict,Any
from fastapi.exceptions import HTTPException as FastAPIHTTPException
from schemas.apiResponse import ErrorResponse

class CustomAppException(FastAPIHTTPException):
    def __init__(
            self,
            status_code: int,
            code: str,
            message: str = None,
            detail: Any = None
    ):
        super().__init__(status_code=status_code, detail=detail)
        self.code = code
        self.message = message if message else code


def add_exception_handlers(app: FastAPI):

    @app.exception_handler(FastAPIHTTPException)
    async def http_exception_handler(request: Request, exc: FastAPIHTTPException):
        if isinstance(exc.detail, dict) and "code" in exc.detail and "status" in exc.detail:
            error_content = exc.detail
        else:
            error_response_model = ErrorResponse(
                status="error",
                code=str(exc.status_code),
                message=exc.detail
            )
            error_content = error_response_model.model_dump()

        return JSONResponse(
            status_code=exc.status_code,
            content=error_content
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        import traceback
        traceback.print_exc()

        error_response_model = ErrorResponse(
            status="error",
            code="INTERNAL_SERVER_ERROR",
            message="An unexpected server error occurred.",
            detail=str(exc)
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=error_response_model.model_dump()
        )
