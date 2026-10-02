from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.models import Transaction, Customer

router = APIRouter()

@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(get_db)):
    total_revenue = db.query(func.sum(Transaction.total_amount)).scalar() or 0.0
    total_orders = db.query(func.count(Transaction.id)).scalar() or 0
    total_customers = db.query(func.count(Customer.id)).scalar() or 0
    aov = (total_revenue / total_orders) if total_orders > 0 else 0.0

    return {
        "total_revenue": round(total_revenue, 2),
        "total_orders": total_orders,
        "total_customers": total_customers,
        "average_order_value": round(aov, 2)
    }