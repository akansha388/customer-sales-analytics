from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.core.database import get_db
from app.models.analytics_models import Order, OrderItem, Product

router = APIRouter()

@router.get("/monthly-revenue")
def get_monthly_revenue(db: Session = Depends(get_db)):
    results = db.query(
        extract('year', Order.order_date).label('year'),
        extract('month', Order.order_date).label('month'),
        func.sum(Order.total_amount).label('total_revenue'),
        func.count(Order.id).label('order_count')
    ).group_by('year', 'month').order_by('year', 'month').all()

    return [
        {
            "period": f"{int(r.year)}-{int(r.month):02d}",
            "revenue": round(float(r.total_revenue), 2),
            "orders": r.order_count
        } for r in results
    ]

@router.get("/sales-by-category")
def get_sales_by_category(db: Session = Depends(get_db)):
    results = db.query(
        Product.category,
        func.sum(OrderItem.total_price).label('total_sales'),
        func.sum(OrderItem.quantity).label('units_sold')
    ).join(OrderItem, Product.id == OrderItem.product_id)\
     .group_by(Product.category).all()

    return [
        {
            "category": r.category,
            "sales": round(float(r.total_sales or 0), 2),
            "units": r.units_sold or 0
        } for r in results
    ]