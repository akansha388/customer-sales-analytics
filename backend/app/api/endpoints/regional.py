from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.analytics_models import Order, Customer

router = APIRouter()

@router.get("/regional-sales")
def get_regional_sales(db: Session = Depends(get_db)):
    results = db.query(
        Order.region,
        func.sum(Order.total_amount).label('total_revenue'),
        func.count(Customer.id.distinct()).label('customer_count'),
        func.count(Order.id).label('order_count')
    ).join(Customer, Order.customer_id == Customer.id)\
     .group_by(Order.region).all()

    return [
        {
            "region": r.region or "Unknown",
            "revenue": round(float(r.total_revenue or 0), 2),
            "customers": r.customer_count,
            "orders": r.order_count
        } for r in results
    ]