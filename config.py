from dotenv import load_dotenv
import os

load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./printflow.db")

# Paper Types and Pricing
PAPER_TYPES = {
    "black_white": {
        "name": "Black & White",
        "price_per_page": 1.00
    },
    "colored": {
        "name": "Colored",
        "price_per_page": 3.00
    },
    "photo": {
        "name": "Photo Paper",
        "price_per_page": 5.00
    }
}

# API Settings
API_TITLE = "PrintFlow API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "Printing shop order management system"
