System rozproszony - Serwis Produktów i Serwis Magazynowy

Opis - prosty system rozproszony składający się z dwóch mikroserwisów:

1. **Serwis Produktów** (`product_service.py`) – udostępnia dane produktów.
2. **Serwis Magazynowy** (`stock_service.py`) – udostępnia stan magazynowy i sprawdza istnienie produktów w Serwisie Produktów.

Wymagania:
- Python 3.7+
- Pakiety: `fastapi`, `uvicorn`, `requests`

Instalacja:

1. Utwórz wirtualne środowisko:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

Zainstaluj wymagane pakiety:
pip install fastapi uvicorn requests

Uruchomienie serwisów:

1. Uruchom Serwis Produktów:
python -m uvicorn product_service:app --reload --port 8001

Uruchom Serwis Magazynowy (w nowym terminalu):
python -m uvicorn stock_service:app --reload --port 8002

Uwaga: Serwis Magazynowy musi mieć dostęp do Serwisu Produktów, dlatego oba serwisy powinny działać jednocześnie.

Testowanie (Postman)
Możesz użyć Postmana do wysyłania zapytań HTTP do serwisów.

Przykładowe zapytania
Sprawdzenie stanu magazynowego istniejącego produktu (sukces):

GET http://127.0.0.1:8002/stock/1
Odpowiedź:

{
  "productId": 1,
  "quantity": 15
}


Sprawdzenie stanu magazynowego nieistniejącego produktu (błąd 404):

GET http://127.0.0.1:8002/stock/999

Odpowiedź:

{
  "detail": "Produkt nie istnieje"
}

















  
  "name": "Laptop",
  "price": 4500.00
}
