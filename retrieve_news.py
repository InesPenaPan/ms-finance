import yfinance as yf
from fastapi import HTTPException, status
from typing import List

def fetch_yfinance_news(ticker_symbol: str, count: int) -> List[dict]:
    """
    Retrieves the most recent news items for a given stock ticker from yfinance,
    formats them into a clean dictionary list, and limits the result count.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        raw_news = stock.news
        
        if not raw_news:
            return []
        
        formatted_news = []
        news_processed = 0
        
        for item in raw_news:
            # Crucial filter: Skip if primary content keys are missing
            content_data = item.get('content')
            if not content_data or not content_data.get("title"):
                continue
            
            if news_processed >= count:
                break 

            thumbnail = content_data.get("thumbnail", {}).get("resolutions", [{}])
            thumbnail_url = thumbnail[0].get("url") if thumbnail and thumbnail[0] else None
            
            publisher_name = content_data.get('provider', {}).get('displayName', 'Unknown')
            link_url = content_data.get('canonicalUrl', {}).get('url', '#')
            
            summary_text = content_data.get("summary", "No summary provided by the source.")
            
            formatted_news.append({
                "title": content_data.get("title", "No Title Available"),
                "summary": summary_text, 
                "link": link_url,
                "publisher": publisher_name,
                "publish_date": content_data.get("pubDate", "1970-01-01T00:00:00Z"),
                "thumbnail_url": thumbnail_url
            })
            
            news_processed += 1
            
        return formatted_news

    except Exception as e:
        print(f"Error in yfinance retrieval for {ticker_symbol}: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to retrieve data for '{ticker_symbol}'. Check ticker or service availability."
        )