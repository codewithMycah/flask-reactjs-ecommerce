from flask import Flask, jsonify, request
from flask_cors import CORS
from lxml import etree

app = Flask(__name__)
CORS(app)

# Load and parse the XML file
def load_xml():
    tree = etree.parse("businesses.xml")
    return tree.getroot()

# Save changes back to the XML file
def save_xml(root):
    tree = etree.ElementTree(root)
    tree.write("businesses.xml", pretty_print=True, encoding="utf-8")

# Read all businesses
@app.route("/businesses", methods=["GET"])
def get_businesses():
    root = load_xml()
    businesses = []
    for business in root.findall("business"):
        businesses.append({
            "id": business.find("id").text,
            "name": business.find("name").text,
            "address": business.find("address").text,
            "phone": business.find("phone").text,
            "email": business.find("email").text,
            "businessType": business.find("businessType").text,
            "businessHours": business.find("businessHours").text,
        })
    return jsonify(businesses)

# Add a new product
@app.route("/businesses", methods=["POST"])
def add_product():
    data = request.json
    root = load_xml()

    new_business = etree.SubElement(root, "business")
    etree.SubElement(new_business, "id").text = str(data["id"])
    etree.SubElement(new_business, "name").text = data["name"]
    etree.SubElement(new_business, "address").text = data["address"]
    etree.SubElement(new_business, "phone").text = data["phone"]
    etree.SubElement(new_business, "email").text = data["email"]
    etree.SubElement(new_business, "businessType").text = data["businessType"]
    etree.SubElement(new_business, "businessHours").text = data["businessHours"]

    save_xml(root)
    return jsonify({"message": "Business added successfully"}), 201

# Update a product
@app.route("/businesses/<int:business_id>", methods=["PUT"])
def update_product(business_id):
    data = request.json
    root = load_xml()

    for business in root.findall("business"):
        if int(business.find("id").text) == business_id:
            business.find("name").text = data["name"]
            business.find("address").text = data["address"]
            business.find("phone").text = data["phone"]
            business.find("email").text = data["email"]
            business.find("businessType").text = data["businessType"]
            business.find("businessHours").text = data["businessHours"]
            save_xml(root)
            return jsonify({"message": "Business updated successfully"}), 200

    return jsonify({"message": "Business not found"}), 404

# Delete a product
@app.route("/businesses/<int:business_id>", methods=["DELETE"])
def delete_product(business_id):
    root = load_xml()

    for business in root.findall("business"):
        if int(business.find("id").text) == business_id:
            root.remove(business)
            save_xml(root)
            return jsonify({"message": "Business deleted successfully"}), 200

    return jsonify({"message": "Business not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
