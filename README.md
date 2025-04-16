# My Multi-Vendor E-Commerce Project

This project is a multi-vendor e-commerce platform built with React for the frontend and Django for the backend. It integrates with HubSpot for CRM, Authorize.Net for payment processing, and ShipStation for shipping management. The design aims to provide a user experience similar to Amazon.

## Project Structure

```
my-multi-vendor-ecommerce
├── frontend                # Frontend React application
│   ├── public             # Public assets
│   ├── src                # Source code for the React app
│   ├── package.json       # NPM configuration for frontend
│   ├── .env               # Environment variables for frontend
│   └── README.md          # Documentation for frontend
├── backend                 # Backend Django application
│   ├── app                # Django app containing models, views, and serializers
│   ├── project            # Django project settings and configuration
│   ├── manage.py          # Command-line utility for Django
│   ├── requirements.txt    # Python dependencies for backend
│   └── README.md          # Documentation for backend
├── integrations            # Integration scripts for external services
│   ├── hubspot.py         # HubSpot CRM integration
│   ├── authorize_net.py   # Authorize.Net payment processing integration
│   └── shipstation.py     # ShipStation shipping integration
└── README.md              # Overall documentation for the project
```

## Features

- **User Registration and Authentication**: Users can create accounts, log in, and manage their profiles.
- **Vendor Management**: Vendors can register, list their products, and manage orders.
- **Product Listings**: Users can browse products, filter by categories, and view product details.
- **Shopping Cart**: Users can add products to their cart and proceed to checkout.
- **Payment Processing**: Integration with Authorize.Net for secure payment transactions.
- **Order Management**: Users can view their order history and track shipments via ShipStation.
- **CRM Integration**: Customer data is managed using HubSpot's CRM API.

## Getting Started

### Prerequisites

- Node.js and npm for the frontend
- Python and Django for the backend
- Access to HubSpot, Authorize.Net, and ShipStation APIs

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-multi-vendor-ecommerce
   ```

2. Set up the frontend:
   ```
   cd frontend
   npm install
   ```

3. Set up the backend:
   ```
   cd backend
   pip install -r requirements.txt
   ```

4. Configure environment variables in `.env` for the frontend and settings in `settings.py` for the backend.

5. Run the applications:
   - Frontend: `npm start`
   - Backend: `python manage.py runserver`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.