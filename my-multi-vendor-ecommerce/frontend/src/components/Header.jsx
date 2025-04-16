import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; // Assuming you will create a CSS file for styling

const Header = () => {
    return (
        <header className="header">
            <div className="logo">
                <Link to="/">My E-Commerce</Link>
            </div>
            <nav className="nav">
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/products">Products</Link></li>
                    <li><Link to="/vendors">Vendors</Link></li>
                    <li><Link to="/about">About Us</Link></li>
                    <li><Link to="/contact">Contact</Link></li>
                </ul>
            </nav>
            <div className="search">
                <input type="text" placeholder="Search products..." />
                <button type="submit">Search</button>
            </div>
            <div className="cart">
                <Link to="/cart">Cart</Link>
            </div>
        </header>
    );
};

export default Header;