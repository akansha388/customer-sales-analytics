import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_code = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String)
    region = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="customer")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_code = Column(String, unique=True, index=True)
    name = Column(String)
    category = Column(String, index=True)
    unit_price = Column(Numeric(10, 2))
    unit_cost = Column(Numeric(10, 2))

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    order_number = Column(String, unique=True, index=True)
    customer_id = Column(String, ForeignKey("customers.id"), index=True)
    order_date = Column(DateTime, index=True)
    total_amount = Column(Numeric(10, 2))
    region = Column(String, index=True)

    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    order_id = Column(String, ForeignKey("orders.id"), index=True)
    product_id = Column(String, ForeignKey("products.id"), index=True)
    quantity = Column(Integer)
    unit_price = Column(Numeric(10, 2))
    unit_cost = Column(Numeric(10, 2))
    total_price = Column(Numeric(10, 2))
    profit = Column(Numeric(10, 2))

    order = relationship("Order", back_populates="items")
    product = relationship("Product")