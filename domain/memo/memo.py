from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MemoBase(BaseModel):
    title: str = "제목 없음"
    content: str = "내용 없음"

class MemoCreate(MemoBase):
    pass

class MemoUpdate(MemoBase):
    title: Optional[str] = None
    content: Optional[str] = None

class Memo(MemoBase):
    id: int
    created_at: datetime
    updated_at: datetime
