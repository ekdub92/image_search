from image_search import utils
from image_search.server.consts import QueryInputType
from image_search.server.dtos import QueryInput
from image_search.server.singleton_store import feature_extractor


def get_query_features(query_input: QueryInput):
    if query_input.input_type == QueryInputType.TEXT:
        text = query_input.query
        query_features = feature_extractor.get_text_features(text)
    elif query_input.input_type == QueryInputType.IMAGE:
        image_url = query_input.query
        image = utils.load_image_from_url(image_url)
        query_features = feature_extractor.get_image_features(image)
    else:
        raise ValueError(f"Unrecognized input type: {query_input.input_type}")
    return query_features
