import React from "react";
import { Link } from "react-router-dom";

import './index.css';


function Register() {
    return (
        <div className="register-container">
            <h1>Register Page</h1>
            <Link to="/">Back to login page</Link>
        </div>
    );
}

export default Register;