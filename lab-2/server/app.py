from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Хранилище данных (в реальном приложении "lab3" использовалась бы БД)
data_store = {}
next_id = 1

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id in data_store:
        return jsonify(data_store[item_id]), 200
    return jsonify({"error": "Item not found"}), 404

@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Bad request"}), 400
    
    item = {
        'id': next_id,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    data_store[next_id] = item
    next_id += 1
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in data_store:
        return jsonify({"error": "Item not found"}), 404
    if not request.json:
        return jsonify({"error": "Bad request"}), 400
    
    data_store[item_id].update({
        'name': request.json.get('name', data_store[item_id]['name']),
        'description': request.json.get('description', data_store[item_id]['description'])
    })
    return jsonify(data_store[item_id]), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in data_store:
        del data_store[item_id]
        return jsonify({"message": "Item deleted"}), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)