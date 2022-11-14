from typing import List

from fastapi import Body, Depends, FastAPI

from ..service_layer import services
from . import dependencies, schemas

app = FastAPI()

@app.put(
    "/indices/{index}",
    tags=["indices"],
    description="Индексироват документ (добавить документ в индекс)"
)
async def add_index(index: str, docs_bulk = Body()):
    ep = dependencies.ep
    return await services.add_doc_to_index(ep, index, docs_bulk)


@app.get(
    "/indices/{index}", 
    tags=["indices"],
    description="Поиск подстроки по всем полям индекса",
    responses=schemas.get_examples
)
async def search_substring_in_index(params: schemas.SearchParams = Depends()):
    ep = dependencies.ep
    return await services.search_index_for_text(ep, params.index, params.text)


