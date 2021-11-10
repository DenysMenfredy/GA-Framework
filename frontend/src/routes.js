import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Login from './pages/login';
import Register from "./pages/register";
import PasswordRecovery from "./pages/passwordRecovery";

export default function PagesRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route exact path="/" element={<Login/>} />
                <Route exact path="/register" element={<Register/>} />
                <Route exact path="/passwordRecovery" element={<PasswordRecovery/>} />
            </Routes>
        </BrowserRouter>
    );
}