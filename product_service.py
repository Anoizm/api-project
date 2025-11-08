from fastapi import FastAPI, HTTPException

app = FastAPI()

products = {
    1: {"id": 1, "name": "Laptop", "price": 4500.00},
    2: {"id": 2, "name": "Mysz", "price": 150.00},
    3: {"id": 3, "name": "Klawiatura", "price": 300.00},
}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produkt nie istnieje")
    return product