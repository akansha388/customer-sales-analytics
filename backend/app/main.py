from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.models import analytics_models  # Import models to register tables

# Create tables in Docker PostgreSQL database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Customer & Sales Analytics API",
    version="1.0.0",
    description="Business Intelligence and Analytics REST API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "online", "database": "PostgreSQL connected"}