from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
import json

app = FastAPI()

# Load product data from products.json
with open('products.json', 'r') as f:
    products_data = json.load(f)

products = products_data['products']

@app.get("/products/search")
async def search_products(desc: str = Query(..., description="Product description to search for")):
    filtered_products = [product for product in products if desc.lower() in product['description'].lower()]
    return filtered_products

@app.get("/products/read")
async def read_product(id: str = Query(..., description="Product ID to read")):
    for product in products:
        if product['id'] == id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8090)