from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data: a simple in-memory "database"
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

# Get all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a specific item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        abort(404)  # Not found
    return jsonify(item)

# Create a new item
@app.route('/api/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        abort(400)  # Bad request
    new_item = {
        "id": items[-1]["id"] + 1,  # Incrementing ID
        "name": request.json["name"],
    }
    items.append(new_item)
    return jsonify(new_item), 201  # Created

# Delete an item by ID
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
