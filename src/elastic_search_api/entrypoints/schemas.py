from fastapi import Query, Path
from pydantic import BaseModel


class SearchParams:
    def __init__(
        self,
        index: str = Path(..., description="Название индекса", example="some-index"),
        text: str = Query(..., description="Текст для поиска", example="любая подстрока")        
    ) -> None:
        self.index = index
        self.text = text
