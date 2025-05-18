# E-commerce Manager FastAPI

FastAPI and MySQL based Ecommerce management app for managing e-commerce sales data, inventory, and product registration — built for powering admin dashboards with rich insights.

## Requirements

Ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)

## 🧱 Tech Stack

- **FastAPI** — Web framework
- **SQLAlchemy** — ORM
- **Alembic** — Database migrations
- **MySQL** — Relational database

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/M-Adil-Sultan/FastAPI-ecommerce-manager
   cd FastAPI-ecommerce-manager
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Move into working directory

   ```bash
   cd app
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Environment file:
   Create .env file in app directory
   Add following environment variables and there values:
   DB_USER =
   DB_PASSWORD =
   DB_HOST =
   DB_PORT =
   DB_NAME =

6. Run Alembic Migrations:
   ```bash
   alembic upgrade head
   ```

## Running the Project

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

## Populate Demo data

open http://127.0.0.1:8000/docs in browser
Try it out and Execute

```
POST api/populate-demo-data
```

## API Endpoints

**Sales Analytics**

- POST api/sales
  ➤ Add New Sale respective to request body
  Sample Request body

```
{
 "store_name": "Amazon",
 "sale_date": "2025-05-17T14:00:00",
 "items": [
   { "product_id": 1, "quantity": 2, "unit_price": 20.0 },
   { "product_id": 2, "quantity": 1, "unit_price": 50.0 }
 ]

```

- Get api/summary :
  ➤ Total number of sales and total revenue.

- GET api/revenue?period=daily|weekly|monthly|yearly
  ➤ Revenue breakdown by selected period.

- GET api/by-filters?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&product_id=&category_id=
  ➤ Sales filtered by product or category within a date range.
  start_date=YYYY-MM-DD
  end_date=YYYY-MM-DD
  product_id=INT
  category_id=INT
