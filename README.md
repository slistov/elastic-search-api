# Elastic searcher API

This is a simple example of API to access elasticsearch service.

The app uses library [elastic-search-lib](https://github.com/slistov/elastic-search-api).

## Install

- clone
- pip install -r requirements.txt

## Run the app

uvicorn src.elastic_search_api.entrypoints.fastapi_app:app

# REST API

Example data is a set of quotes taken from movies.

API's goal is to give user a tool for searching quotes for any text specified.

The REST API to the example app is described below.

## Get list of quotes, containing text provided

### Request

`GET /quotes`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/quotes/?text=erm
    
### Response

    HTTP/1.1 200 OK
    date: Fri, 18 Nov 2022 12:24:32 GMT
    server: uvicorn
    content-length: 163
    content-type: application/json

    [
      {
        "speaker":"The Terminator",
        "quote":"Аста ла виста, бейби.",
        "movie":"Терминатор 2: Судный день",
        "stuff":["Прощание"]
      }
    ]
