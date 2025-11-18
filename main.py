from fastapi import FastAPI, HTTPException, status, Query
from models.model_finance import FinancialData
from models.model_news import StockNewsResponse
from calculate_ratios import calculate_ratios, calculate_growth_history 
from retrieve_news import fetch_yfinance_news

# FastAPI initialization
app = FastAPI(
    title="Finance API Microservice",
)

# ----------------------------------------------------------------------
# Financial Data Endpoint
# ----------------------------------------------------------------------

@app.get(
    "/finance/{ticker}", 
    response_model=FinancialData, 
    summary="Calculates current ratios, T0 vs T-1 comparison, and quarterly revenue growth history"
)

def get_financial_results(ticker: str):
    ticker_upper = ticker.upper()

    try:
        comparison_data = calculate_ratios(ticker_upper)
        historical_data = calculate_growth_history(ticker_upper)
        
        results = {
            "ticker": ticker_upper, 
            **comparison_data,
            **historical_data,
        }
        return results
        
    except ValueError as ve:
        raise HTTPException(
            status_code=404, 
            detail=f"Error: Data for ticker '{ticker}' is incomplete or lacks historical depth. Details: {ve}"
        )
    except Exception as e:
        print(f"Unhandled error for {ticker}: {e}")
        raise HTTPException(
            status_code=500, 
            detail=f"Internal Server Error processing ticker: {ticker_upper}."
        )
    
# ----------------------------------------------------------------------
# Stock news Endpoint
# ----------------------------------------------------------------------

@app.get(
    "/news/{ticker}", 
    response_model=StockNewsResponse,
    summary="Get recent news headlines and links"
)
def get_stock_news_endpoint(
    ticker: str, 
    limit: int = Query(5, ge=1, le=10, description="Maximum number of headlines to return (1-10)")
):
    ticker_upper = ticker.upper()

    try:
        headlines_data = fetch_yfinance_news(ticker_upper, count=limit)
        
        return StockNewsResponse(
            ticker=ticker_upper,
            count=len(headlines_data),
            latest_headlines=headlines_data,
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Unexpected server error when processing '{ticker_upper}'. Detail: {e}"
        )
