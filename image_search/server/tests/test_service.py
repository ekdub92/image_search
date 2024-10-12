from image_search.server.consts import QueryInputType
from image_search.server.dtos import QueryInput
from image_search.server.service import get_query_features


class TestGetQueryFeatures:
    def test_text_features_should_not_zeros(self):
        # GIVEN
        query_input = QueryInput(input_type=QueryInputType.TEXT, query="cat")

        # WHEN
        query_features = get_query_features(query_input)

        # THEN
        assert all(feature for feature in query_features if feature != 0)

    def test_image_features_should_not_zeros(self):
        # GIVEN
        cat_image_url = "https://flexible.img.hani.co.kr/flexible/normal/970/777/imgdb/resize/2019/0926/00501881_20190926.JPG"
        query_input = QueryInput(input_type=QueryInputType.IMAGE, query=cat_image_url)

        # WHEN
        query_features = get_query_features(query_input=query_input)

        # THEN
        assert all(feature for feature in query_features if feature != 0)
