import pandas as pd
import requests

def get_external_data(url):
    """
    Fetches data from an external URL and returns it as a pandas DataFrame if it's JSON.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if isinstance(data, list):
            return pd.DataFrame(data)
        else:
            return pd.DataFrame([data])
            
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def process_stats(df):
    """
    Performs basic descriptive statistics on a DataFrame.
    """
    if df.empty:
        return "No data available."
    return df.describe().to_dict()
