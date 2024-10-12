from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from image_search.server import settings
from image_search.server.consts import INDEX_NAME


class Searcher:
    def __init__(self):
        self.client = Elasticsearch(
            hosts=[settings.ES_ENDPOINT],
#             http_auth=(settings.ES_USERNAME, settings.ES_PASSWORD),
            verify_certs=False,
        )
        self.index_name = INDEX_NAME

    def create_index(self):
        knn_index = {
            "settings": {
                "index.knn": True,
            },
            "mappings": {
                "properties": {
                    "feature_vector": {
                        "type": "knn_vector",
                        "dimension": 512,
                    }
                }
            },
        }
        return self.client.indices.create(index=self.index_name, body=knn_index, ignore=400)

    def bulk_ingest(self, generate_data, chunk_size=128):
        return bulk(self.client, generate_data, chunk_size=chunk_size)

    def knn_search(self, query_features, k=10):
        source = {
            "exclude": ["feature_vector"],
        }

        query = {
            "field": "feature_vector",
            "query_vector": query_features,
            "k": k,
            "num_candidates": 100
        }
        return self.client.knn_search(index=self.index_name, knn=query, source=source)
