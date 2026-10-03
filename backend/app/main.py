from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import dashboard, sales, customers, products, regional, transactions

app = FastAPI(title="Executive Analytics Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(sales.router, prefix="/api/sales", tags=["Sales"])
app.include_router(customers.router, prefix="/api/customers", tags=["Customers"])
app.include_router(products.router, prefix="/api/products", tags=["Products"])
app.include_router(regional.router, prefix="/api/regional", tags=["Regional"])
app.include_router(transactions.router, prefix="/api/transactions", tags=["Transactions"])