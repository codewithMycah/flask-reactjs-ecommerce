import React, { useEffect, useState } from "react";
import axios from "axios";

const BusinessList = () => {
    const [business, setBusiness] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:5000/businesses")
            .then((response) => setBusiness(response.data))
            .catch((error) => console.error(error));
    }, []);

    return (
        <div>
            <h1>Businesses</h1>
            <ul>
                {business.map((business) => (
                    <li key={business.id}>
                        <h2>{business.name}</h2>
                        <p>Address: ${business.address}</p>
                        <p>Phone: {business.phone}</p>
                        <p>Email: {business.email}</p>
                        <p>Business Type: {business.businessType}</p>
                        <p>Business Hours: {business.businessHours}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default BusinessList;
