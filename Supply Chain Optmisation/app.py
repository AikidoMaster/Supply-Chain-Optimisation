from flask import Flask, request, jsonify
from utils.data_processing import load_data
from optimization.optimizer import optimize_transportation
import os

app = Flask(__name__)

# Path to the dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'train.csv')

@app.route('/process_data', methods=['GET'])
def process_data():
    try:
        data = load_data(DATA_PATH)
        return jsonify({"message": "Data processed successfully!", "columns": list(data.columns)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/optimize', methods=['POST'])
def optimize():
    try:
        payload = request.json
        costs = payload['costs']
        demand = payload['demand']
        supply = payload['supply']
        
        result = optimize_transportation(costs, demand, supply)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
