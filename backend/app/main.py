from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import dashboard, sales, customers, products, regional, transactions

app = FastAPI(title="Customer & Sales Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["Dashboard"])
app.include_router(sales.router, prefix="/api/v1/sales", tags=["Sales"])
app.include_router(customers.router, prefix="/api/v1/customers", tags=["Customers"])
app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(regional.router, prefix="/api/v1/regional", tags=["Regional"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["Transactions"])

@app.get("/")
def read_root():
    return {"status": "online", "database": "PostgreSQL connected"}