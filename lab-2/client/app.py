from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
SERVER_URL = 'http://server:5000/items'

@app.route('/items', methods=['GET'])
def get_items():
    try:
        response = requests.get(SERVER_URL)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    try:
        response = requests.get(f'{SERVER_URL}/{item_id}')
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Bad request"}), 400
    try:
        response = requests.post(SERVER_URL, json=request.json)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if not request.json:
        return jsonify({"error": "Bad request"}), 400
    try:
        response = requests.put(f'{SERVER_URL}/{item_id}', json=request.json)
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        response = requests.delete(f'{SERVER_URL}/{item_id}')
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)