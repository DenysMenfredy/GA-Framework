import React, { useState, useEffect } from 'react';
import { Link, useHistory } from 'react-router-dom';

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
                        <div className="form-group">
                            <label htmlFor="exampleInputEmail1">Email address</label>
                            <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="exampleInputPassword1">Password</label>
                            <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Password" />
                        </div>
                        <div className="form-group">
                            <div className="form-check">
                                <label htmlFor="remember-check">Remember me</label>
                                <input type="checkbox" id="remember-check" />
                            </div>
                            <Link className="link" to="/passwordRecovery">Forgot password?</Link>
                        </div>
                        <div className="form-group">
                            <button type="submit" className="login-btn">Login</button>
                        </div>
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