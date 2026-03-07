from config import PAPER_TYPES

def calculate_order_cost(pages: int, paper_type: str) -> float:
    """
    Calculate the total cost of a print order.
    
    Args:
        pages: Number of pages to print
        paper_type: Type of paper (black_white, colored, photo)
        
    Returns:
        Total cost in currency units
    """
    if paper_type not in PAPER_TYPES:
        raise ValueError(f"Invalid paper type: {paper_type}")
    
    price_per_page = PAPER_TYPES[paper_type]["price_per_page"]
    total_cost = pages * price_per_page
    
    return round(total_cost, 2)

def get_paper_info(paper_type: str) -> dict:
    """Get information about a paper type."""
    if paper_type not in PAPER_TYPES:
        raise ValueError(f"Invalid paper type: {paper_type}")
    
    return PAPER_TYPES[paper_type]

def get_all_paper_types() -> dict:
    """Get all available paper types."""
    return PAPER_TYPES
