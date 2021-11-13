import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import FormField from '../../components/FormField';
import FormButton from '../../components/FormButton';

import './index.css';

import google from '../../assets/google-logo.png';

function Login() {

    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

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
                    <img src={google} alt="google logo" />
                    <h4>Login with Google</h4>
                    {/* <p>or</p> */}
                </div>
                <h5>or</h5>
                <div className="login-form">
                    <form>
                            <FormField
                                label="Email"
                                type="email"
                                name="email"
                                onChange={(e) => { setEmail(e.target.value) }}
                                value={email}
                            />
                            <FormField
                                label="Password"
                                type="password"
                                name="password"
                                onChange={(e) => {setPassword(e.target.value)}}
                                value={password}
                            />
                        
                        <div className="form-check">
                            <div className="form-check-input">
                                <input type="checkbox" id="remember-check" />
                                <label htmlFor="remember-check">Remember me</label>
                            </div>
                            <Link className="link" to="/passwordRecovery">Forgot password?</Link>
                        </div>
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