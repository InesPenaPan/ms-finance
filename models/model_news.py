from pydantic import BaseModel
from typing import List, Optional

class HeadlineItem(BaseModel):
    """
    Schema defining the structure of a single news headline item retrieved 
    from the source.
    """
    title: str
    summary: str 
    link: str
    publisher: str
    publish_date: str 
    thumbnail_url: Optional[str] = None

class StockNewsResponse(BaseModel):
    """
    The complete API response structure for the /news/{ticker} endpoint.
    It wraps the list of headlines along with metadata about the query.
    """
    ticker: str
    count: int
    latest_headlines: List[HeadlineItem]