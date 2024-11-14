from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/sample_db"
mongo = PyMongo(app)


def init_db():
    if mongo.db.products.count_documents({}) == 0:
        products = [
            {
                "name": "Chips",
                "price": 1.09,
                "category": "Sneks",
                "stock": 50,
            },
            {
                "name": "Apples",
                "price": 0.99,
                "category": "Fruits",
                "stock": 200,
            },
            {
                "name": "Oranges",
                "price": 1.49,
                "category": "Fruits",
                "stock": 100,
            }
        ]
        mongo.db.products.insert_many(products)

    if mongo.db.orders.count_documents({}) == 0:
        orders = [
            {
                "customer_name": "John Doe",
                "products": ["Apples", "Honey"],
                "total_amount": 20.98,
                "status": "completed",
            },
            {
                "customer_name": "Jane Smith",
                "products": ["Spaghetti"],
                "total_amount": 6.99,
                "status": "pending",
            }
        ]
        mongo.db.orders.insert_many(orders)


@app.route('/api/products', methods=['GET'])
def get_products():
    products = list(mongo.db.products.find())
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products)


@app.route('/api/products/<category>', methods=['GET'])
def get_products_by_category(category):
    products = list(mongo.db.products.find({"category": category}))
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products)


@app.route('/api/products/stock/<int:threshold>', methods=['GET'])
def get_low_stock_products(threshold):
    products = list(mongo.db.products.find({"stock": {"$lt": threshold}}))
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products)


@app.route('/api/products/create', methods=['GET'])
def create_product():
    try:
        new_product = {
            "name": request.args.get('name'),
            "price": float(request.args.get('price')),
            "category": request.args.get('category'),
            "stock": int(request.args.get('stock', 0)),
        }

        if not all([new_product['name'], new_product['price'], new_product['category']]):
            return jsonify({"error": "Missing required fields"}), 400

        result = mongo.db.products.insert_one(new_product)
        new_product['_id'] = str(result.inserted_id)

        return jsonify({
            "message": "Product created successfully",
            "product": new_product
        })
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/products/delete/<product_id>', methods=['GET'])
def delete_product(product_id):
    try:
        product_obj_id = ObjectId(product_id)

        product = mongo.db.products.find_one({"_id": product_obj_id})
        if not product:
            return jsonify({"error": "Product not found"}), 404

        result = mongo.db.products.delete_one({"_id": product_obj_id})

        if result.deleted_count == 1:
            return jsonify({
                "message": "Product deleted successfully",
                "deleted_id": product_id
            })
        else:
            return jsonify({"error": "Failed to delete product"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/products/delete/category/<category>', methods=['GET'])
def delete_products_by_category(category):
    try:
        count = mongo.db.products.count_documents({"category": category})
        if count == 0:
            return jsonify({"error": "No products found in this category"}), 404

        result = mongo.db.products.delete_many({"category": category})

        return jsonify({
            "message": f"Successfully deleted {result.deleted_count} products",
            "deleted_count": result.deleted_count,
            "category": category
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/orders', methods=['GET'])
def get_orders():
    orders = list(mongo.db.orders.find())
    for order in orders:
        order['_id'] = str(order['_id'])
    return jsonify(orders)


@app.route('/api/orders/status/<status>', methods=['GET'])
def get_orders_by_status(status):
    orders = list(mongo.db.orders.find({"status": status}))
    for order in orders:
        order['_id'] = str(order['_id'])
    return jsonify(orders)


@app.route('/api/orders/customer/<name>', methods=['GET'])
def get_orders_by_customer(name):
    orders = list(mongo.db.orders.find({"customer_name": name}))
    for order in orders:
        order['_id'] = str(order['_id'])
    return jsonify(orders)


@app.route('/api/orders/create', methods=['GET'])
def create_order():
    try:
        products = request.args.get('products', '').split(',')
        products = [p.strip() for p in products if p.strip()]

        new_order = {
            "customer_name": request.args.get('customer_name'),
            "products": products,
            "total_amount": float(request.args.get('total_amount')),
            "status": request.args.get('status', 'pending'),
        }

        if not all([new_order['customer_name'], new_order['products'], new_order['total_amount']]):
            return jsonify({"error": "Missing required fields"}), 400

        result = mongo.db.orders.insert_one(new_order)
        new_order['_id'] = str(result.inserted_id)

        return jsonify({
            "message": "Order created successfully",
            "order": new_order
        })
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/orders/delete/<order_id>', methods=['GET'])
def delete_order(order_id):
    try:
        order_obj_id = ObjectId(order_id)

        order = mongo.db.orders.find_one({"_id": order_obj_id})
        if not order:
            return jsonify({"error": "Order not found"}), 404

        result = mongo.db.orders.delete_one({"_id": order_obj_id})

        if result.deleted_count == 1:
            return jsonify({
                "message": "Order deleted successfully",
                "deleted_id": order_id
            })
        else:
            return jsonify({"error": "Failed to delete order"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/orders/delete/status/<status>', methods=['GET'])
def delete_orders_by_status(status):
    try:
        count = mongo.db.orders.count_documents({"status": status})
        if count == 0:
            return jsonify({"error": f"No orders found with status '{status}'"}), 404

        result = mongo.db.orders.delete_many({"status": status})

        return jsonify({
            "message": f"Successfully deleted {result.deleted_count} orders",
            "deleted_count": result.deleted_count,
            "status": status
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/products/create/bulk', methods=['GET'])
def create_multiple_products():
    try:
        # name1:price1:category1:stock1,name2:price2:category2:stock2
        products_data = request.args.get('products', '').split(',')
        new_products = []

        for product_str in products_data:
            if not product_str.strip():
                continue
            name, price, category, stock = product_str.split(':')
            new_product = {
                "name": name.strip(),
                "price": float(price),
                "category": category.strip(),
                "stock": int(stock),
            }
            new_products.append(new_product)

        if not new_products:
            return jsonify({"error": "No valid products provided"}), 400

        result = mongo.db.products.insert_many(new_products)

        return jsonify({
            "message": f"Successfully created {len(result.inserted_ids)} products",
            "product_ids": [str(id) for id in result.inserted_ids]
        })
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
