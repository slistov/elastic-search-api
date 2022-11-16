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
    stuff1: str
    stuff2: str


get_examples = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "examples": {
                        "success": {
                            "summary": "Найдены соответствия",
                            "value": {
                                "took": 3,
                                "timed_out": False,
                                "_shards": {
                                    "total": 1,
                                    "successful": 1,
                                    "skipped": 0,
                                    "failed": 0
                                },
                                "hits": {
                                    "total": {
                                        "value": 1,
                                        "relation": "eq"
                                    },
                                    "max_score": 2.0605695,
                                    "hits": [
                                        {
                                            "_index": "quote-ind3",
                                            "_id": "exoAdoQB9S5BtCTeVYMK",
                                            "_score": 2.0605695,
                                            "_source": {
                                                "speaker": "Gollum",
                                                "quote": "Оно пришло ко мне, моя собственность, моя любовь… моя прелесть...",
                                                "movie": "Властелин колец: Братство кольца",
                                                "stuff1": "Обладание",
                                                "stuff2": "Любовь"
                                            }
                                        }
                                    ]
                                }
                            }
                        },
                        "notfound": {
                            "summary": "Не найдено соответствий",
                            "value": {
                                "took": 1,
                                "timed_out": False,
                                "_shards": {
                                    "total": 1,
                                    "successful": 1,
                                    "skipped": 0,
                                    "failed": 0
                                },
                                "hits": {
                                    "total": {
                                        "value": 0,
                                        "relation": "eq"
                                    },
                                    "max_score": "null",
                                    "hits": []
                                }
                                }
                        },
                    }
                }
            }
        },
    }
