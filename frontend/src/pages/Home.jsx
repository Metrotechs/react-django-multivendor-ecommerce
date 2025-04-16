import React from 'react';
import Header from '../components/Header';

const Home = () => {
    return (
        <div>
            <Header />
            <h1>Welcome to Our Multi-Vendor E-commerce Platform</h1>
            <div className="promotional-banner">
                <h2>Check out our latest deals!</h2>
            </div>
            <div className="product-listings">
                <h2>Featured Products</h2>
                {/* Product listings will be rendered here */}
            </div>
        </div>
    );
};

export default Home;