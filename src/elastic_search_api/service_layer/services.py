from elastic_search_lib.services import ElasticProvider

from ..domain import model


class ElasticParser:
    """Elastic response parser

    Contains parse methods
    """
    @classmethod
    def parse_response(cls, response):
        """Parse elastic response
        Returns: List of [hits][hits][_source] """
        return [item['_source'] for item in response['hits']['hits']]


async def add_doc_to_index(
    ep: ElasticProvider,
    docs_bulk,
    index='quotes-index'
):
    """Index bulk of docs

    Adds several docs (bulk) into index"""
    try:
        await ep.get_index_by_name(index)
    except Exception:
        i = model.IndexQuote(index)
        await ep.add_index(i.name, i.mappings, i.settings)
    return await ep.add_docs_bulk(index=index, docs_bulk=docs_bulk)


async def search_index_for_text(ep: ElasticProvider, index, text):
    """Search index for text

    Searches text inside index"""
    elastic_response = await ep.search(index=index, text=text, fields=["*"])
    return ElasticParser.parse_response(elastic_response)
