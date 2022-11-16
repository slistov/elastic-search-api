from fastapi import APIRouter, Body, Depends

from .. import config
from ..service_layer import services
from . import dependencies, schemas

quotes_router = APIRouter(
    prefix=config.get_quotes_path(),
    tags=["quotes"]
)


@quotes_router.put(
    "/",
    tags=["quotes"],
    description="Индексировать документ (добавить документ в индекс)"
)
async def add_index(docs_bulk=Body()):
    ep = dependencies.ep
    return await services.add_doc_to_index(
        ep=ep,
        docs_bulk=docs_bulk,
        index=config.QUOTES_INDEX
    )


@quotes_router.get(
    "/",
    tags=["quotes"],
    description="Поиск подстроки по всем полям индекса",
    responses=schemas.get_examples
)
async def search_substring_in_index(params: schemas.SearchParams = Depends()):
    ep = dependencies.ep
    return await services.search_index_for_text(
        ep=ep,
        text=params.text,
        index=config.QUOTES_INDEX
    )
