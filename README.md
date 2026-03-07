<<<<<<< HEAD
This is the readme file...
=======
# PrintFlow API

A FastAPI-based backend system for managing printing shop orders with automatic cost calculation.

## Features

- **Order Management**: Create, read, update, and delete printing orders
- **Automatic Cost Calculation**: Automatically calculates printing costs based on page count and paper type
- **Paper Type Support**: 
  - Black & White ($1.00 per page)
  - Colored ($3.00 per page)
  - Photo Paper ($5.00 per page)
- **Order Tracking**: Track order status (pending, processing, completed, cancelled)
- **Customer Access**: Customers can view their orders by email
- **Shop Analytics**: View shop statistics, revenue by paper type, and order status breakdown
- **RESTful API**: Clean, documented API with OpenAPI/Swagger documentation

## Project Structure

```
Activity_FastAPI/
├── main.py                 # FastAPI application entry point
├── config.py              # Configuration settings and constants
├── database.py            # Database setup and SQLAlchemy models
├── schemas.py             # Pydantic models for request/response validation
├── utils.py               # Utility functions (cost calculation, etc.)
├── routes/
│   ├── __init__.py
│   ├── orders.py          # Order management endpoints
│   ├── paper_types.py     # Paper type information endpoints
│   └── admin.py           # Shop analytics and statistics endpoints
├── requirements.txt       # Python dependencies
├── .env.example          # Environment configuration template
└── README.md             # This file
```

## Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd c:\xampp\htdocs\Activity_FastAPI
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   copy .env.example .env
   ```
   Edit `.env` if needed (default SQLite database is fine for development)

## Running the Application

Start the FastAPI server:

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The application will start on `http://localhost:8000`

## API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI JSON**: http://localhost:8000/api/openapi.json

## API Endpoints

### Orders
- `POST /orders/` - Create a new order
- `GET /orders/` - Get all orders (with pagination and filtering)
- `GET /orders/{order_id}` - Get order by ID
- `PUT /orders/{order_id}` - Update an order
- `DELETE /orders/{order_id}` - Cancel an order
- `GET /orders/by-email/{customer_email}` - Get orders by customer email

### Paper Types
- `GET /paper-types/` - Get all available paper types and pricing
- `GET /paper-types/{paper_type}` - Get specific paper type details

### Admin/Analytics
- `GET /admin/stats` - Get shop statistics
- `GET /admin/revenue-by-type` - Get revenue breakdown by paper type
- `GET /admin/pending-orders` - Get all pending orders
- `GET /admin/status-summary` - Get order summary by status

## Example API Calls

### Create an Order
```bash
curl -X POST "http://localhost:8000/orders/" \
  -H "Content-Type: application/json" \
  -d {
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "pages": 50,
    "paper_type": "colored",
    "notes": "Urgent printing"
  }
```

### Get All Paper Types
```bash
curl "http://localhost:8000/paper-types/"
```

### Get Shop Statistics
```bash
curl "http://localhost:8000/admin/stats"
```

### Get Orders by Customer Email
```bash
curl "http://localhost:8000/orders/by-email/john@example.com"
```

## Database

The application uses SQLAlchemy ORM with SQLite by default (configurable via `DATABASE_URL` in `.env`).

Database schema includes:
- **Orders Table**: Stores all printing orders with customer details, page count, paper type, calculated cost, status, and timestamps

## Configuration

Edit `config.py` to customize:
- Paper types and pricing
- Database connection details (via `.env`)
- API settings and metadata

## Users & Roles

The system is designed for:
- **Customers**: Can create orders and view their own orders
- **Shop Staff**: Can view and manage all orders
- **Shop Owner**: Can view analytics and manage all orders

*(Authentication/authorization can be added as a future enhancement)*

## Future Enhancements

- [ ] User authentication and authorization
- [ ] Order status notifications
- [ ] Payment integration
- [ ] File upload for print templates
- [ ] Order scheduling and pickup dates
- [ ] Discount and promo code support
- [ ] Advanced analytics and reporting
- [ ] Email notifications
- [ ] Multi-language support

## Technologies Used

- **Framework**: FastAPI 0.104+
- **Server**: Uvicorn
- **Database**: SQLAlchemy + SQLite
- **Validation**: Pydantic
- **API Documentation**: Swagger UI (OpenAPI)

## License

This project is created for educational purposes.

## Support

For issues or questions, please refer to the API documentation at `/api/docs`
>>>>>>> 5cab967 (First Commit)
