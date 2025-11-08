from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

stock_data = {
    1: 15,
    2: 50,
    3: 30,
}

PRODUCT_SERVICE_URL = "http://127.0.0.1:8001/products/"

@app.get("/stock/{product_id}")
def get_stock(product_id: int):
    try:
        response = requests.get(f"{PRODUCT_SERVICE_URL}{product_id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Produkt nie istnieje")
        response.raise_for_status()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Błąd komunikacji z Serwisem Produktów")

    quantity = stock_data.get(product_id, 0)
    return {"productId": product_id, "quantity": quantity}