import os

import yaml
from dotenv import load_dotenv

load_dotenv()
config = yaml.safe_load(
    open("src/elastic_search_api/config.yaml", mode="r", encoding="utf-8")
)

QUOTES_INDEX = config['QUOTES_INDEX']


def get_es_uri():
    host = os.environ.get("ELASTIC_HOST", "https://0.0.0.0")
    port = os.environ.get("ELASTIC_PORT", "9200")
    return f"{host}:{port}"


def get_es_user_credentials():
    user = os.environ.get("ELASTIC_USER", "elastic")
    password = os.environ.get("ELASTIC_PASSWORD", "Set ELASTIC_PASSWORD in .env file")
    return f"{user}", f"{password}"


# PATHS
def get_root_path():
    return config["ROOT_PATH"]


def get_quotes_path():
    root = config["ROOT_PATH"]
    quotes = config["QUOTES_PATH"]
    return f"{root}{quotes}"
