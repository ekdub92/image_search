import logging
from fastapi import FastAPI, Response, status

from image_search.server.feature_processing.searcher import Searcher
from image_search.server.dtos import QueryInput
from image_search.server.service import get_query_features

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root(input_type: str, query: str, response: Response):
    query_input = QueryInput(input_type=input_type, query=query)
    try:
        query_features = get_query_features(query_input)
    except Exception as e:
        logger.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Error when processing input."}

    try:
        searcher = Searcher()
        response = searcher.knn_search(query_features[0], k=10)
        results = response["hits"]["hits"]
        return {
            "message": "Success",
            "body": results,
        }
    except Exception as e:
        logger.error(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Search engine error."}
