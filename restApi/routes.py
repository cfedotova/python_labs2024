from flask import Flask, request, jsonify
from file import File

app = Flask(__name__)
file = File()


@app.route('/api/items', methods=['GET'])
def get_items():
    try:
        items = file.read_data()
        return jsonify(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    try:
        items = file.read_data()
        item = next((item for item in items if item.get('id') == item_id), None)
        if item:
            return jsonify(item), 200
        return jsonify({"error": "Item not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/items', methods=['POST'])
# {"age": "20", "city": "Lviv", "description": "Student", "name": "Vasyl"}
def create_item():
    try:
        items = file.read_data()
        new_item = request.get_json()

        new_id = 1 if not items else max(item['id'] for item in items) + 1
        new_item['id'] = new_id

        items.append(new_item)
        file.write_data(items)

        return jsonify(new_item), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/items/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    try:
        items = file.read_data()
        item = next((item for item in items if item.get('id') == item_id), None)

        if not item:
            return jsonify({"error": "Item not found"}), 404

        updates = request.get_json()
        item.update(updates)
        file.write_data(items)

        return jsonify(item), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        items = file.read_data()
        item = next((item for item in items if item.get('id') == item_id), None)

        if not item:
            return jsonify({"error": "Item not found"}), 404

        items = [item for item in items if item.get('id') != item_id]
        file.write_data(items)

        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500
