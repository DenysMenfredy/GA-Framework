import React from 'react';
import { Link } from 'react-router-dom';

import './index.css'


function PasswordRecovery() {
    return (
        <>
            <h1>Recovery your password</h1>
            <Link to="/">Back to login page</Link>
        </>
    );
}

export default PasswordRecovery;

