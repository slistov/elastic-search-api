from fastapi import Body, FastAPI

from ..service_layer import services
from . import dependencies

app = FastAPI()

@app.put("/indices/{index}")
async def api_indexes_add(index: str, docs_bulk = Body()):
    ep = dependencies.ep
    return await services.add_doc_to_index(ep, index, docs_bulk)


@app.get("/indices/{index}")
async def api_search_index_for_text(index, text):
    ep = dependencies.ep
    return await services.search_index_for_text(ep, index, text)


