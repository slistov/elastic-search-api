from elastic_search_lib import ElasticProvider
from elasticsearch import NotFoundError

from ..domain import model


async def add_doc_to_index(ep: ElasticProvider, index_name, docs_bulk):
    try:
        index = await ep.get_index_by_name(index_name)
    except NotFoundError:
        index = model.IndexQuote(index_name)
        await ep.add_index(index.index_name, index.mappings, index.settings)
    return await ep.add_docs_bulk(index_name=index_name, docs_bulk=docs_bulk)


async def search_index_for_text(ep: ElasticProvider, index_name, text):
    return await ep.search(index_name=index_name, text=text)