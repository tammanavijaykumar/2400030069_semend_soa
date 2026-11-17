from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Product Service is running!"})

@app.route("/products")
def products():
    return jsonify({
        "service": "Product Service",
        "product_id": 201,
        "product_name": "Laptop",
        "price": 50000
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
