import React from 'react';
import { Link, useLocation } from 'react-router-dom';

import '../styles/Navbar.css';


const Navbar = () => {
    const location = useLocation();
    const isHomePage = location.pathname === '/';

    return (
        <nav className="navbar">
            <Link to="/" className="navbar-logo">
                jakNajtaniej
            </Link>
            {isHomePage && (
                <div className="navbar-buttons">
                <Link to="/login" className="navbar-button">Login</Link>
                <Link to="/register" className="navbar-button">Register</Link>
                </div>
            )}
        </nav>
        
    );
};

export default Navbar;