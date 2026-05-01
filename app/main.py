from flask import Flask, jsonify
import numpy as np
import pandas as pd
from app.utils import get_external_data, process_stats

app = Flask(__name__)

@app.route('/')
def index():
    # Simple logic using numpy
    random_data = np.random.rand(5, 5)
    mean_val = np.mean(random_data)
    
    # Simple logic using pandas
    df = pd.DataFrame(random_data, columns=[f'col_{i}' for i in range(5)])
    
    return jsonify({
        "message": "Welcome to the Dependency Test App!",
        "numpy_mean": float(mean_val),
        "pandas_preview": df.head(1).to_dict(orient='records'),
        "status": "Running with outdated dependencies"
    })

@app.route('/test-utils')
def test_utils():
    # Example using requests and pandas via utils
    url = "https://jsonplaceholder.typicode.com/posts/1"
    df = get_external_data(url)
    stats = process_stats(df)
    
    return jsonify({
        "data_stats": stats
    })

if __name__ == '__main__':
    print("Starting app on http://127.0.0.1:5000")
    app.run(debug=True)
