"""
Example script to test PrintFlow API

Run the main application first: python main.py
Then run this script to test the API
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def print_response(title, response):
    """Helper function to print API responses"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    try:
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)
    print(f"Status Code: {response.status_code}\n")

def test_api():
    """Test all API endpoints"""
    
    # Test 1: Get all paper types
    response = requests.get(f"{BASE_URL}/paper-types/")
    print_response("Get All Paper Types", response)
    
    # Test 2: Get specific paper type
    response = requests.get(f"{BASE_URL}/paper-types/colored")
    print_response("Get Colored Paper Type", response)
    
    # Test 3: Create an order (Black & White)
    order_data_1 = {
        "customer_name": "John Doe",
        "customer_email": "john@example.com",
        "pages": 50,
        "paper_type": "black_white",
        "notes": "Standard printing"
    }
    response = requests.post(f"{BASE_URL}/orders/", json=order_data_1)
    print_response("Create Order 1 - Black & White", response)
    order_1_id = response.json()["id"] if response.status_code == 200 else None
    
    # Test 4: Create another order (Colored)
    order_data_2 = {
        "customer_name": "Jane Smith",
        "customer_email": "jane@example.com",
        "pages": 30,
        "paper_type": "colored",
        "notes": "Color brochures"
    }
    response = requests.post(f"{BASE_URL}/orders/", json=order_data_2)
    print_response("Create Order 2 - Colored", response)
    order_2_id = response.json()["id"] if response.status_code == 200 else None
    
    # Test 5: Create another order (Photo Paper)
    order_data_3 = {
        "customer_name": "Bob Wilson",
        "customer_email": "bob@example.com",
        "pages": 10,
        "paper_type": "photo",
        "notes": "Photo printing"
    }
    response = requests.post(f"{BASE_URL}/orders/", json=order_data_3)
    print_response("Create Order 3 - Photo Paper", response)
    order_3_id = response.json()["id"] if response.status_code == 200 else None
    
    # Test 6: Get all orders
    response = requests.get(f"{BASE_URL}/orders/")
    print_response("Get All Orders", response)
    
    # Test 7: Get specific order
    if order_1_id:
        response = requests.get(f"{BASE_URL}/orders/{order_1_id}")
        print_response(f"Get Order {order_1_id}", response)
    
    # Test 8: Update order status
    if order_1_id:
        update_data = {"status": "processing"}
        response = requests.put(f"{BASE_URL}/orders/{order_1_id}", json=update_data)
        print_response(f"Update Order {order_1_id} Status", response)
    
    # Test 9: Get orders by customer email
    response = requests.get(f"{BASE_URL}/orders/by-email/john@example.com")
    print_response("Get Orders by Email (john@example.com)", response)
    
    # Test 10: Get shop statistics
    response = requests.get(f"{BASE_URL}/admin/stats")
    print_response("Get Shop Statistics", response)
    
    # Test 11: Get revenue by paper type
    response = requests.get(f"{BASE_URL}/admin/revenue-by-type")
    print_response("Get Revenue by Paper Type", response)
    
    # Test 12: Get pending orders
    response = requests.get(f"{BASE_URL}/admin/pending-orders")
    print_response("Get Pending Orders", response)
    
    # Test 13: Get status summary
    response = requests.get(f"{BASE_URL}/admin/status-summary")
    print_response("Get Status Summary", response)
    
    # Test 14: Health check
    response = requests.get(f"{BASE_URL}/health")
    print_response("Health Check", response)
    
    # Test 15: Root endpoint
    response = requests.get(f"{BASE_URL}/")
    print_response("Root Endpoint", response)
    
    print("\n" + "="*60)
    print("  API Testing Complete!")
    print("="*60)
    print("\nAccess the interactive API documentation at:")
    print(f"  Swagger UI: {BASE_URL}/api/docs")
    print(f"  ReDoc: {BASE_URL}/api/redoc")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the API server.")
        print("Make sure the application is running: python main.py")
    except Exception as e:
        print(f"\nError: {e}")
