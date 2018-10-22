## Installation
Install the library from requirements.txt

## Migration
From the source directory migrate database using manage.py
```buildoutcfg
python manage.py migrate
```
## API
- Get All Users [GET] Method
```buildoutcfg
http://127.0.0.1:8000/api/v1/users
```
- Get Single User [GET] Method
```buildoutcfg
http://127.0.0.1:8000/api/v1/user/<id>
```
- Update User [PUT] Method *Auth Required
```buildoutcfg
http://127.0.0.1:8000/api/v1/auth/user/<id>
```

- Delete User [DELETE] Method *Auth Required
```buildoutcfg
http://127.0.0.1:8000/api/v1/auth/user/<id>
```
- Create User [POST] Method
```buildoutcfg
http://127.0.0.1:8000/api/v1/users
```

- Login User [POST] Method *username & password
```buildoutcfg
http://127.0.0.1:8000/api/v1/auth/login
```

#### Orders Auth Required
- Order Lists [GET] Method
```buildoutcfg
http://127.0.0.1:8000/api/v1/orders
```

- Order Create [POST] Method
```buildoutcfg
http://127.0.0.1:8000/api/v1/orders
```
- Order Update [PUT] Method
```buildoutcfg
http://127.0.0.1:8000/api/v1/order/<id>
```
- Single Order [GET] Method
```buildoutcfg
http://127.0.0.1:8000/api/v1/order/<id>
```
- Cancel Order [DELETE] Method
```buildoutcfg
http://127.0.0.1:8000/api/v1/order/<id>
```

