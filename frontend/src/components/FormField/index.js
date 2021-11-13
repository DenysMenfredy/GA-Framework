import React from "react";
import { FaEnvelope, FaLock } from 'react-icons/fa';

import './index.css';

function FormField({label, type, name, value, onChange}) {
    const fieldId = `id_${name}`;
    return (
        <div className="field">
            <input 
                type={type}
                name={name}
                id={fieldId}
                value={value}
                onChange={onChange}
                />
            {type == 'email' && <FaEnvelope />}
            {type == 'password' && <FaLock />}
            <label htmlFor={fieldId}>{label}</label>
        </div>
    );

}

export default FormField;