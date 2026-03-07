from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import Order, get_db
from schemas import OrderCreate, OrderResponse, OrderUpdate, PaperTypeInfo
from utils import calculate_order_cost, get_all_paper_types
from config import PAPER_TYPES

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderResponse, summary="Create a new print order")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """
    Create a new printing order. 
    Automatically calculates the total cost based on pages and paper type.
    """
    try:
        total_cost = calculate_order_cost(order.pages, order.paper_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    db_order = Order(
        customer_name=order.customer_name,
        customer_email=order.customer_email,
        pages=order.pages,
        paper_type=order.paper_type,
        total_cost=total_cost,
        notes=order.notes
    )
    
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    return db_order

@router.get("/", response_model=list[OrderResponse], summary="Get all orders")
def get_all_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status: str = Query(None),
    db: Session = Depends(get_db)
):
    """Retrieve all orders with optional filtering by status."""
    query = db.query(Order)
    
    if status:
        query = query.filter(Order.status == status)
    
    orders = query.offset(skip).limit(limit).all()
    return orders

@router.get("/{order_id}", response_model=OrderResponse, summary="Get order by ID")
def get_order(order_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific order by ID."""
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return order

@router.put("/{order_id}", response_model=OrderResponse, summary="Update an order")
def update_order(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    """Update an existing order (staff/owner only)."""
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Update fields if provided
    if order_update.customer_name:
        order.customer_name = order_update.customer_name
    if order_update.customer_email:
        order.customer_email = order_update.customer_email
    if order_update.pages or order_update.paper_type:
        pages = order_update.pages or order.pages
        paper_type = order_update.paper_type or order.paper_type
        order.pages = pages
        order.paper_type = paper_type
        order.total_cost = calculate_order_cost(pages, paper_type)
    if order_update.status:
        order.status = order_update.status
    if order_update.notes:
        order.notes = order_update.notes
    
    db.commit()
    db.refresh(order)
    
    return order

@router.delete("/{order_id}", summary="Cancel an order")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    """Cancel/delete an order."""
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(order)
    db.commit()
    
    return {"message": "Order cancelled successfully"}

@router.get("/by-email/{customer_email}", response_model=list[OrderResponse], summary="Get orders by customer email")
def get_orders_by_email(customer_email: str, db: Session = Depends(get_db)):
    """Retrieve all orders for a specific customer by email."""
    orders = db.query(Order).filter(Order.customer_email == customer_email).all()
    
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this customer")
    
    return orders
