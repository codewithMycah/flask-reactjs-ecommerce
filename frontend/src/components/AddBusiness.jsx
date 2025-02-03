import React, { useState } from "react";
import axios from "axios";

const AddBusiness = () => {
    const [formData, setFormData] = useState({
        id: "",
        name: "",
        address: "",
        phone: "",
        email: "",
        businessType: "",
        businessHours: "",
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post("http://127.0.0.1:5000/businesses", formData,
            {
                headers: {
                    'Content-Type': 'application/json',
                },
            }
        )
            .then(() => alert("Business added successfully"))
            .catch((error) => console.error(error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input name="id" placeholder="ID" onChange={handleChange} />
            <input name="name" placeholder="Name" onChange={handleChange} />
            <input name="address" placeholder="Address" onChange={handleChange} />
            <input name="phone" placeholder="Phone" onChange={handleChange} />
            <input name="email" placeholder="Email" onChange={handleChange} />
            <input name="businessType" placeholder="Business Type" onChange={handleChange} />
            <input name="businessHours" placeholder="Business Hours" onChange={handleChange} />

            {/* <textarea name="description" placeholder="Description" onChange={handleChange}></textarea> */}
            <button type="submit">Add Business</button>
        </form>
    );
};

export default AddBusiness;
