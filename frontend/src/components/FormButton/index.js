import React from "react";

import './index.css';


function FormButton({text, onClick}) {
    return (
        <div>
            <button className="form-button" onClick={onClick}>{text}</button>
        </div>
    );
}

export default FormButton;
