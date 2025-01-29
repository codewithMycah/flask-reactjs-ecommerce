import React, { useState } from "react";
import axios from "axios";

const AddProduct = () => {
    const [formData, setFormData] = useState({
        id: "",
        name: "",
        price: "",
        stock: "",
        description: ""
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post("http://127.0.0.1:5000/products", formData)
            .then(() => alert("Product added successfully"))
            .catch((error) => console.error(error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input name="id" placeholder="ID" onChange={handleChange} />
            <input name="name" placeholder="Name" onChange={handleChange} />
            <input name="price" placeholder="Price" onChange={handleChange} />
            <input name="stock" placeholder="Stock" onChange={handleChange} />
            <textarea name="description" placeholder="Description" onChange={handleChange}></textarea>
            <button type="submit">Add Product</button>
        </form>
    );
};

export default AddProduct;
