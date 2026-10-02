from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.analytics_models import Customer, Order

router = APIRouter()

@router.get("/top-customers")
def get_top_customers(limit: int = 10, db: Session = Depends(get_db)):
    results = db.query(
        Customer.id,
        Customer.name,
        Customer.email,
        Customer.region,
        func.sum(Order.total_amount).label('total_spent'),
        func.count(Order.id).label('total_orders')
    ).join(Order, Customer.id == Order.customer_id)\
     .group_by(Customer.id)\
     .order_by(func.sum(Order.total_amount).desc())\
     .limit(limit).all()

    return [
        {
            "id": r.id,
            "name": r.name,
            "email": r.email,
            "region": r.region,
            "total_spent": round(float(r.total_spent or 0), 2),
            "total_orders": r.total_orders
        } for r in results
    ]