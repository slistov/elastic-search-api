from elasticsearch import AsyncElasticsearch, NotFoundError
from elas

from ..domain import model


async def add_doc_to_index(ep: ElasticIndexRepositoryAbstract, index_name, docs_bulk):
    try:
        index = await elastic_repo.get_index_by_name(index_name)
    except NotFoundError:
        index = model.IndexQuote(index_name, docs_bulk)
        await elastic_repo.add(index)
    return await elastic_repo.add_docs_bulk(index_name=index_name, docs_bulk=docs_bulk)


async def search_index_for_text(elastic_repo: ElasticIndexRepositoryAbstract, index_name, text):
    return await elastic_repo.search(index_name=index_name, text=text)