import React from "react";


import './index.css';

function FormField({label, type, name, value, onChange}) {
    const fieldId = `id_${name}`;
    return (
        <div>
            <input 
                type={type}
                name={name}
                id={fieldId}
                value={value}
                onChange={onChange}
                />
            <label htmlFor={fieldId}>{label}</label>
        </div>
    );

}

export default FormField;