from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import Optional

class PaperTypeEnum(str, Enum):
    black_white = "black_white"
    colored = "colored"
    photo = "photo"

class OrderCreate(BaseModel):
    customer_name: str = Field(..., min_length=1, max_length=100)
    customer_email: str = Field(..., min_length=5)
    pages: int = Field(..., gt=0, description="Number of pages to print")
    paper_type: PaperTypeEnum
    notes: Optional[str] = Field(None, max_length=500)

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    pages: Optional[int] = None
    paper_type: Optional[PaperTypeEnum] = None
    status: Optional[str] = None
    notes: Optional[str] = None

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    pages: int
    paper_type: str
    total_cost: float
    status: str
    created_at: datetime
    notes: Optional[str] = None

    class Config:
        from_attributes = True

class PaperTypeInfo(BaseModel):
    code: str
    name: str
    price_per_page: float

class OrderStats(BaseModel):
    total_orders: int
    total_revenue: float
    pending_orders: int
    completed_orders: int
