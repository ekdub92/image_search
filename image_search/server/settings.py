import os

from dotenv import load_dotenv

load_dotenv()

# Elastic Search
ES_ENDPOINT = os.environ.get("ES_ENDPOINT", "http://localhost:9200")
# ES_USERNAME = os.environ.get("ES_USERNAME", "elastic")
# ES_PASSWORD = os.environ["ES_PASSWORD"]
