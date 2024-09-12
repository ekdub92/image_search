from pydantic import BaseModel, Field

from clip_image_search.server.consts import QueryInputType


class QueryInput(BaseModel):
    input_type: QueryInputType = Field(default=QueryInputType.TEXT, description="query 입력 타입")
    query: str = Field(description="query. image는 url로 제공")
