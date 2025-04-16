# Backend Multi-Vendor E-commerce Project

This is the backend component of the multi-vendor e-commerce website built using Django. The backend is responsible for handling data management, business logic, and integration with third-party services.

## Project Structure

- **app/**: Contains the main application code.
  - **models.py**: Defines the data models for products, vendors, and orders.
  - **views.py**: Contains the view functions or class-based views for handling requests and responses.
  - **urls.py**: Defines the URL routing for the application.
  - **serializers.py**: Contains serializers for converting complex data types into JSON format.

- **project/**: Contains the Django project settings and configuration.
  - **settings.py**: Configuration settings for the Django project, including database settings and installed apps.
  - **urls.py**: Main URL routing for the Django project.
  - **wsgi.py**: Entry point for WSGI-compatible web servers.

- **manage.py**: Command-line utility for interacting with the Django project.

- **requirements.txt**: Lists the Python dependencies required for the backend application.

## Features

- Multi-vendor support for product listings.
- Integration with HubSpot for CRM functionalities.
- Payment processing through Authorize.Net.
- Shipping management via ShipStation.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-multi-vendor-ecommerce/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Integration

- Ensure to configure the necessary API keys and settings for HubSpot, Authorize.Net, and ShipStation in the `settings.py` file.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.