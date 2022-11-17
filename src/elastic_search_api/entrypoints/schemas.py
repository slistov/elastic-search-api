from typing import List

from fastapi import Query
from pydantic import BaseModel


class SearchParams:
    def __init__(
        self,
        text: str = Query(
            ...,
            description="Текст для поиска",
            example="любая подстрока"
        )
    ) -> None:
        self.text = text


class Quote(BaseModel):
    speaker: str
    quote: str
    movie: str
    stuff: List[str]
