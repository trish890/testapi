from fastapi import APIRouter
from schemas import PaperTypeInfo
from utils import get_all_paper_types

router = APIRouter(prefix="/paper-types", tags=["Paper Types"])

@router.get("/", response_model=dict, summary="Get all paper types and pricing")
def get_paper_types():
    """
    Retrieve all available paper types with their pricing information.
    """
    paper_types = get_all_paper_types()
    
    result = {}
    for code, info in paper_types.items():
        result[code] = {
            "code": code,
            "name": info["name"],
            "price_per_page": info["price_per_page"]
        }
    
    return result

@router.get("/{paper_type}", response_model=PaperTypeInfo, summary="Get paper type details")
def get_paper_type(paper_type: str):
    """
    Get details for a specific paper type.
    """
    paper_types = get_all_paper_types()
    
    if paper_type not in paper_types:
        return {"detail": "Paper type not found"}, 404
    
    info = paper_types[paper_type]
    return {
        "code": paper_type,
        "name": info["name"],
        "price_per_page": info["price_per_page"]
    }
