from pydantic import BaseModel
from typing import Optional, List

class SimpleComparison(BaseModel):
    """
    A model used to compare a financial metric between the 
    current reporting period (T0) and the previous period (T-1).
    """
    current_value: Optional[float] = None
    previous_value: Optional[float] = None

class FinancialData(BaseModel):
    """
    The main response model for the /finance/{ticker} endpoint.
    It aggregates various financial ratios, performance metrics, 
    and historical growth data.
    """
    ticker: str
    
    current_ratio: SimpleComparison = SimpleComparison() 
    quick_ratio: SimpleComparison = SimpleComparison()   
    debt_to_equity: SimpleComparison = SimpleComparison()
    market_cap: SimpleComparison = SimpleComparison()

    report_dates: Optional[List[str]] = None
    quarterly_revenue_growth: Optional[List[Optional[float]]] = None