from typing import Dict, List, Optional
from domain.memo.memo import Memo, MemoCreate, MemoUpdate
from datetime import datetime


class MemoryDB:
    def __init__(self):
        self.memos_db: Dict[int,Memo] = {}
        self.index : int = 0

    def create_memo(self,memo_create:MemoCreate) -> Memo:
        self.index += 1
        current_time = datetime.now()

        new_memo = Memo(
            id=self.index,
            title=memo_create.title,
            content=memo_create.content,
            created_at=current_time,
            updated_at=current_time
        )

        self.memos_db[self.index] = new_memo
        return new_memo


    def get_memo_list(self) -> List[Memo]:
        return list(self.memos_db.values())


    def get_memo(self,memo_id:int) -> Optional[Memo]:
        return self.memos_db.get(memo_id)

    def update_memo(self,memo_id:int,memo_update:MemoUpdate) -> Optional[Memo]:
        memo_to_update = self.memos_db.get(memo_id)
        if not memo_to_update:
            return None

        if memo_update.title is not None:
            memo_to_update.title = memo_update.title
        if memo_update.content is not None:
            memo_to_update.content = memo_update.content

        memo_to_update.updated_at = datetime.now()

        self.memos_db[memo_id] = memo_to_update
        return memo_to_update


    def delete_memo(self, memo_id: int) -> bool:
        if memo_id not in self.memos_db:
            return False
        del self.memos_db[memo_id]
        return True
