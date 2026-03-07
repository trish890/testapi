from fastapi import FastAPI
<<<<<<< HEAD
app = FastAPI()

@app.get("/")
async def read_root():
  return{"message": "Welcome to your first FastApi applicant!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
  return{"item_id": item_id, "query": q}

@app.get("/multiply/{a}/{b}")
async def multiply_numbers(a: int, b: int):
  return {"result": a * b}
=======
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
from config import API_TITLE, API_VERSION, API_DESCRIPTION
from routes import orders, paper_types, admin

# Create FastAPI application
app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description=API_DESCRIPTION,
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables on startup
@app.on_event("startup")
def startup_event():
    create_tables()
    print("Database tables created successfully")

# Include routers
app.include_router(orders.router)
app.include_router(paper_types.router)
app.include_router(admin.router)

# Root endpoint
@app.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint for PrintFlow API"""
    return {
        "message": "Welcome to PrintFlow API",
        "version": API_VERSION,
        "description": API_DESCRIPTION,
        "endpoints": {
            "orders": "/orders",
            "paper_types": "/paper-types",
            "admin": "/admin",
            "documentation": "/api/docs"
        }
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> 5cab967 (First Commit)
