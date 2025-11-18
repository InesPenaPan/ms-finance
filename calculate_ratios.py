import yfinance as yf
import numpy as np
from typing import Dict, Any, Optional, List
from models.model_finance import SimpleComparison 

# HELPER FUNCTIONS

def safe_div(numerator, denominator):
    """
    Safely performs division. Returns None if the denominator is zero.
    Rounds the result to 3 decimal places if division is possible.
    """
    return None if denominator == 0 else round(numerator / denominator, 3)

def safe_div_np(numerator, denominator):
    """
    Safely performs division for NumPy operations. Returns np.nan if 
    the denominator is zero.
    """
    return np.nan if denominator == 0 else (numerator / denominator)

def get_ratio_values(data: Dict[Any, Any], ratio_type: str) -> Optional[float]:
    """
    Calculates specific financial ratios from a dictionary containing 
    balance sheet data for a single period.
    """
    current_assets = data.get('Current Assets', 0)
    current_liabilities = data.get('Current Liabilities', 0)
    inventory = data.get('Inventory', 0)
    total_debt = data.get('Total Debt', 0) 
    total_equity = data.get('Stockholders Equity', 0) 

    if ratio_type == 'current_ratio':
        # Formula: Current Assets / Current Liabilities
        return safe_div(current_assets, current_liabilities)
    elif ratio_type == 'quick_ratio':
        # Formula: (Current Assets - Inventory) / Current Liabilities
        quick_assets = current_assets - inventory
        return safe_div(quick_assets, current_liabilities)
    elif ratio_type == 'debt_to_equity':
        # Formula: Total Debt / Stockholders Equity
        return safe_div(total_debt, total_equity)
    return None

def make_comparison(current, previous):
    """
    Formats the current and previous values into a dictionary 
    matching the SimpleComparison Pydantic model structure.
    """
    return {"current_value": current, "previous_value": previous}


# CALCULATE RATIOS

def calculate_ratios(ticker: str) -> Dict[str, Any]:
    """
    Fetches balance sheet data and basic stock info for a given ticker 
    and calculates current (T0) vs. previous (T-1) financial ratios
    and Market Cap comparison.
    """
    
    try:
        stock = yf.Ticker(ticker)
        balance_sheet = stock.balance_sheet
        stock_info = stock.info
        
        if balance_sheet.empty or len(balance_sheet.columns) < 1:
            raise ValueError("No financial balance sheet data found.")
            
        data_available = len(balance_sheet.columns)
        
        # Data for the latest reporting period (T0)
        data_T0 = balance_sheet.iloc[:, 0].to_dict()
        # Data for the previous reporting period (T-1)
        data_T_1 = balance_sheet.iloc[:, 1].to_dict() if data_available >= 2 else {}
        
        results = {}
        
        # Liquidity & Solvency Ratios
        for ratio_name in ['current_ratio', 'quick_ratio', 'debt_to_equity']:
            val_T0 = get_ratio_values(data_T0, ratio_name)
            val_T_1 = get_ratio_values(data_T_1, ratio_name) if data_available >= 2 else None
            
            results[ratio_name] = make_comparison(val_T0, val_T_1)

        # Market Cap Comparison
        market_cap_current = stock_info.get('marketCap')
        market_cap_previous = stock_info.get('enterpriseValue') 
        
        results['market_cap'] = make_comparison(market_cap_current, market_cap_previous)

        return results
            
    except Exception as e:
        print(f"Error processing punctual data for {ticker}: {e}")
        raise e

# TIME SERIES

def calculate_growth_history(ticker: str) -> Dict[str, Any]:
    """
    Fetches quarterly financial data and calculates the quarter-over-quarter 
    revenue growth rate history.
    """
    try:
        stock = yf.Ticker(ticker)
        quarterly_financials = stock.quarterly_financials 
        
        if quarterly_financials.empty or 'Total Revenue' not in quarterly_financials.index:
            return {"report_dates": None, "quarterly_revenue_growth": None}
            
        revenue_series = quarterly_financials.loc['Total Revenue'].iloc[::-1] 
        
        growth_rates = []
        dates = []
        
        for i in range(1, len(revenue_series)):
            current_revenue = revenue_series.iloc[i]
            previous_revenue = revenue_series.iloc[i-1]
            
            # Calculate growth: (Current - Previous) / Previous
            growth = safe_div_np(current_revenue - previous_revenue, previous_revenue)
            
            growth_rates.append(growth)
            dates.append(revenue_series.index[i].strftime('%Y-%m-%d'))
            
        # Clean up numpy NaNs and round final results to 3 decimals
        final_growth = [None if np.isnan(v) else round(v, 3) for v in growth_rates]

        return {
            "report_dates": dates,
            "quarterly_revenue_growth": final_growth,
        }
            
    except Exception as e:
        print(f"Error calculating growth history for {ticker}: {e}")
        return {"report_dates": None, "quarterly_revenue_growth": None}