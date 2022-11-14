from elastic_search_lib import ElasticProvider
from elasticsearch import AsyncElasticsearch

from .. import config

user, password = config.get_es_user_credentials()
es = AsyncElasticsearch(
    config.get_es_uri(), 
    basic_auth=(user, password),
    verify_certs=False
)

ep = ElasticProvider(es)
