# Sample online Store

## Checkout repo
```
git clone git@github.com:cequoi-ca/boutique.git
```

# Services

## Login Service  

The login service shall handle user authentication

### API Endpoints

### /signup

A signup request sent from a user with an email as json body,
shall result in a new user being created in the database
```
{
  "user": "email"
}
```

### /signin

A signin request sent from a user with an email as json body,
shall result in new tooken beein generated for the user.
The login service will generate a token and store the token with the user in the database.
The response to the signin is a request with token
```
{
  "token": "aabbccddeeffgghh"
}
```

A client that have signed in and received a token, will use the token in the http header
Authorization: 
```
Authorization: "bearer aabbccddeeffgghh"
```

When a client access a service, the service shall check for the header Authorization and fetch the token.
Thereafter the service shalll query the database to find the user that's assocoated with the token.


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
