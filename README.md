# Sample online Store

# Services

## Cart Service

Running manually
```bash
cd cart-service
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

Runnig with docker compose
```
docker compose build cart-service
docker compose up 
```

## Product Catalog Service

Running manually
```bash
cd product-catalog-service
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

Runnig with docker compose
```
docker compose build product-catalog-service
docker compose up 
```