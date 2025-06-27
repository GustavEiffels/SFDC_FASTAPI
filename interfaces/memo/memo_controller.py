from fastapi import APIRouter, HTTPException, status
from typing import Dict, List, Optional
from domain.memo.memo import Memo, MemoUpdate, MemoCreate
from schemas.apiResponse import DataResponse, ListResponse, ErrorResponse, BaseResponse
from  infra.InMemory import MemoryDB

router = APIRouter()
memo_service = MemoryDB()

@router.get("/list",response_model=ListResponse, summary="모든 메모 조회")
async def read_memos():
    memo_list = memo_service.get_memo_list()
    return ListResponse(data=memo_list,total_count=len(memo_list))

@router.get("/{memo_id}",summary="특정 메모 조회",response_model=DataResponse)
async def read_memo(memo_id:int):
    memo = memo_service.get_memo(memo_id)
    if memo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="메모를 찾을 수 없습니다.")
    return DataResponse(data=memo)

@router.post("/",summary="메모 생성",response_model=DataResponse)
async def create_memo(memo_create:MemoCreate):
    return DataResponse(data=memo_service.create_memo(memo_create))

@router.put("/{memo_id}",summary="메모 수정",response_model=DataResponse)
async def update_memo(memo_id:int, memo_update:MemoUpdate):
    updated_memo = memo_service.update_memo(memo_id, memo_update)
    if updated_memo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="메모를 찾을 수 없습니다.")
    return DataResponse(data=updated_memo)

@router.delete("/memos/{memo_id}", status_code=status.HTTP_204_NO_CONTENT, summary="메모 삭제")
async def delete_memo_endpoint(memo_id: int):
    success = memo_service.delete_memo(memo_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="메모를 찾을 수 없습니다.")
    return