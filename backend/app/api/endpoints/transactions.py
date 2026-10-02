from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.analytics_models import Order, Customer

router = APIRouter()

@router.get("/")
def get_transactions(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    results = db.query(
        Order.id,
        Order.order_number,
        Order.order_date,
        Customer.name.label('customer_name'),
        Order.region,
        Order.total_amount
    ).join(Customer, Order.customer_id == Customer.id)\
     .order_by(Order.order_date.desc())\
     .offset(skip).limit(limit).all()

    return [
        {
            "id": r.id,
            "order_number": r.order_number,
            "date": r.order_date.strftime("%Y-%m-%d %H:%M") if r.order_date else "",
            "customer": r.customer_name,
            "region": r.region,
            "total_amount": float(r.total_amount or 0)
        } for r in results
    ]