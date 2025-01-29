from flask import Flask, jsonify, request
from flask_cors import CORS
from lxml import etree

app = Flask(__name__)
CORS(app)

# Load and parse the XML file
def load_xml():
    tree = etree.parse("products.xml")
    return tree.getroot()

# Save changes back to the XML file
def save_xml(root):
    tree = etree.ElementTree(root)
    tree.write("products.xml", pretty_print=True, encoding="utf-8")

# Read all products
@app.route("/products", methods=["GET"])
def get_products():
    root = load_xml()
    products = []
    for product in root.findall("product"):
        products.append({
            "id": product.find("id").text,
            "name": product.find("name").text,
            "price": float(product.find("price").text),
            "stock": int(product.find("stock").text),
            "description": product.find("description").text,
        })
    return jsonify(products)

# Add a new product
@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    root = load_xml()

    new_product = etree.SubElement(root, "product")
    etree.SubElement(new_product, "id").text = str(data["id"])
    etree.SubElement(new_product, "name").text = data["name"]
    etree.SubElement(new_product, "price").text = str(data["price"])
    etree.SubElement(new_product, "stock").text = str(data["stock"])
    etree.SubElement(new_product, "description").text = data["description"]

    save_xml(root)
    return jsonify({"message": "Product added successfully"}), 201

# Update a product
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.json
    root = load_xml()

    for product in root.findall("product"):
        if int(product.find("id").text) == product_id:
            product.find("name").text = data["name"]
            product.find("price").text = str(data["price"])
            product.find("stock").text = str(data["stock"])
            product.find("description").text = data["description"]
            save_xml(root)
            return jsonify({"message": "Product updated successfully"}), 200

    return jsonify({"message": "Product not found"}), 404

# Delete a product
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    root = load_xml()

    for product in root.findall("product"):
        if int(product.find("id").text) == product_id:
            root.remove(product)
            save_xml(root)
            return jsonify({"message": "Product deleted successfully"}), 200

    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
