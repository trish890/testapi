from fastapi import FastAPI
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