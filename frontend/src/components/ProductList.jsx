import React, { useEffect, useState } from "react";
import axios from "axios";

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:5000/products")
            .then((response) => setProducts(response.data))
            .catch((error) => console.error(error));
    }, []);

    return (
        <div>
            <h1>Products</h1>
            <ul>
                {products.map((product) => (
                    <li key={product.id}>
                        <h2>{product.name}</h2>
                        <p>Price: ${product.price}</p>
                        <p>Stock: {product.stock}</p>
                        <p>{product.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProductList;
