from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.analytics_models import Product, OrderItem

router = APIRouter()

@router.get("/top-products")
def get_top_products(limit: int = 10, db: Session = Depends(get_db)):
    results = db.query(
        Product.id,
        Product.name,
        Product.category,
        Product.unit_price,
        func.sum(OrderItem.quantity).label('total_units_sold'),
        func.sum(OrderItem.total_price).label('total_revenue'),
        func.sum(OrderItem.profit).label('total_profit')
    ).join(OrderItem, Product.id == OrderItem.product_id)\
     .group_by(Product.id)\
     .order_by(func.sum(OrderItem.total_price).desc())\
     .limit(limit).all()

    return [
        {
            "id": r.id,
            "name": r.name,
            "category": r.category,
            "unit_price": float(r.unit_price or 0),
            "units_sold": r.total_units_sold or 0,
            "total_revenue": round(float(r.total_revenue or 0), 2),
            "total_profit": round(float(r.total_profit or 0), 2)
        } for r in results
    ]