import React, { useState, useEffect } from 'react';
import { Link, useHistory } from 'react-router-dom';

import FormField from '../../components/FormField';
import FormButton from '../../components/FormButton';

import './index.css';

function Login() {
    return (
        <section className="login-container">
            <div className="left-side">
                <h1>LOGO HERE </h1>
            </div>
            <div className="right-side">
                <div className="login-text">
                    <h2>Log in to...</h2>
                    <p>Welcome back! login with your data that you entered during registration.</p>
                </div>
                <div className="google-login">
                    <h4>Login with Google</h4>
                    {/* <p>or</p> */}
                </div>
                <div className="login-form">
                    <form>
                            <FormField
                                label="Email"
                                type="email"
                                name="email"
                                onChange={() => { }}
                                value=""
                            />
                            <FormField
                                label="Password"
                                type="password"
                                name="password"
                                onChange={() => { }}
                                value=""
                            />
                        
                        <div className="form-check">
                            <label htmlFor="remember-check">Remember me</label>
                            <input type="checkbox" id="remember-check" />
                        </div>
                            <Link className="link" to="/passwordRecovery">Forgot password?</Link>
                        <FormButton 
                            text="Login"
                        />
                    </form>
                    <div className="register-opt">
                        <p>Don't have an account? <Link className="link" to="/register">Register</Link></p>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Login;