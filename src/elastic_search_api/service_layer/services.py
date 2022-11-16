from elastic_search_lib.services import ElasticProvider
from elasticsearch import NotFoundError

from ..domain import model


async def add_doc_to_index(ep: ElasticProvider, docs_bulk, index='quotes-index'):
    try:
        await ep.get_index_by_name(index)
    except NotFoundError:
        i = model.IndexQuote(index)
        await ep.add_index(i.name, i.mappings, i.settings)
    return await ep.add_docs_bulk(index=index, docs_bulk=docs_bulk)


async def search_index_for_text(ep: ElasticProvider, index, text):
    response = await ep.search(index=index, text=text, fields=["*"])
    return response