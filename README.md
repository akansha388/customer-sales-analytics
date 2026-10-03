# Executive Analytics Dashboard

A full-stack business analytics web application designed for interactive data visualization and sales tracking. Built with FastAPI on the backend and React with Tailwind CSS on the frontend, connected to a PostgreSQL database.

## Project Architecture

The repository is divided into two primary subdirectories:

* backend - Contains the FastAPI application, database connections, SQLAlchemy ORM models, and API endpoints.
* frontend - Contains the React single-page application built with Vite, TypeScript, and Tailwind CSS v4.

Inside the backend directory, the application code resides within the app directory. This contains:
* api - Endpoint routes grouped into individual routers such as dashboard, sales, customers, products, regional, and transactions.
* core - Database setup and session configuration using SQLAlchemy.
* models - Database schemas defining tables for Customers, Products, Orders, and Order Items.

Inside the frontend directory, the user interface code sits in the src directory, containing component layouts, state management, and API integration logic.

## Prerequisites

Make sure you have the following installed on your machine:

* Python 3.13 or later
* Node.js (v18 or later) and npm
* PostgreSQL server

## Getting Started

### 1. Database Setup

Create a PostgreSQL database named `customer_analytics` (or update your configuration in `backend/app/core/database.py` with your database credentials).

### 2. Backend Setup

Open a terminal and navigate to the backend folder:

cd backend

Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

Install the required Python packages:

pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic

Start the FastAPI development server:

uvicorn app.main:app --reload --port 8000

The backend API will run at http://localhost:8000. You can access interactive API documentation at http://localhost:8000/docs.

### 3. Frontend Setup

Open a second terminal and navigate to the frontend folder:

cd frontend

Install dependencies:

npm install

Start the Vite development server:

npm run dev

The frontend web app will run at http://localhost:5173.

## Key Features

* Executive Overview - Live summary metrics for revenue, total orders, customer count, and average order value.
* Sales Analytics - Detailed monthly revenue breakdowns and category performance.
* Customer Tracking - Top customer lists and spending records.
* Product Performance - Units sold, revenue per product, and profit margins.
* Regional Metrics - Location-based sales summaries.
* Recent Transactions - Historical order logs with quick sorting.

## License

This project is licensed under the MIT License.