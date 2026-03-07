from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import Order, get_db
from schemas import OrderStats

router = APIRouter(prefix="/admin", tags=["Admin/Analytics"])

@router.get("/stats", response_model=OrderStats, summary="Get shop statistics")
def get_shop_stats(db: Session = Depends(get_db)):
    """
    Get overall shop statistics including total orders, revenue, and order status breakdown.
    Accessible by shop owner and staff.
    """
    total_orders = db.query(func.count(Order.id)).scalar() or 0
    total_revenue = db.query(func.sum(Order.total_cost)).scalar() or 0.0
    pending_orders = db.query(func.count(Order.id)).filter(Order.status == "pending").scalar() or 0
    completed_orders = db.query(func.count(Order.id)).filter(Order.status == "completed").scalar() or 0
    
    return {
        "total_orders": total_orders,
        "total_revenue": round(total_revenue, 2),
        "pending_orders": pending_orders,
        "completed_orders": completed_orders
    }

@router.get("/revenue-by-type", summary="Get revenue breakdown by paper type")
def get_revenue_by_type(db: Session = Depends(get_db)):
    """
    Get revenue breakdown for each paper type.
    """
    results = db.query(
        Order.paper_type,
        func.count(Order.id).label("order_count"),
        func.sum(Order.total_cost).label("total_revenue")
    ).group_by(Order.paper_type).all()
    
    data = {}
    for paper_type, count, revenue in results:
        data[paper_type] = {
            "order_count": count,
            "total_revenue": round(revenue or 0, 2)
        }
    
    return data

@router.get("/pending-orders", summary="Get all pending orders")
def get_pending_orders(db: Session = Depends(get_db)):
    """
    Get all orders that are still pending processing.
    """
    orders = db.query(Order).filter(Order.status == "pending").all()
    
    return {
        "count": len(orders),
        "orders": orders
    }

@router.get("/status-summary", summary="Get order summary by status")
def get_status_summary(db: Session = Depends(get_db)):
    """
    Get a breakdown of orders by their current status.
    """
    statuses = ["pending", "processing", "completed", "cancelled"]
    summary = {}
    
    for status in statuses:
        count = db.query(func.count(Order.id)).filter(Order.status == status).scalar() or 0
        summary[status] = count
    
    return summary
