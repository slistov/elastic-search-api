from elastic_search_lib.services import ElasticProvider

from .. import config

user, password = config.get_es_user_credentials()

ep = ElasticProvider(
    config.get_es_uri(),
    user,
    password,
    verify_certs=False
)
