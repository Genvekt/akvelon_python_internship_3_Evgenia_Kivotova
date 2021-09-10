# Finance Management web service
![](https://img.shields.io/github/pipenv/locked/dependency-version/Genvekt/akvelon_python_internship_3_Evgenia_Kivotova/django?color=blue&label=Django) ![](https://img.shields.io/github/pipenv/locked/python-version/Genvekt/akvelon_python_internship_3_Evgenia_Kivotova)

REST API for finance management with tocken authentification buided with 
Django REST Framework, Djoger, Swagger with PostgreSQL as Data Storage. Wraped
with Docker. 

## Project structure
```
.
├── docs/                   # Documentation files
├── finance_site            # Django application
│   │
│   ├── finance_site/       # Configuration package
│   │   ├── __init__.py     # Package initialisation
│   │   ├── asgi.py         # 
│   │   ├── settings.py     # Application settings
│   │   ├── urls.py         # Application routing manager
│   │   └── wsgi.py         #  
│   │
│   ├── finance_manager/    # Package for managing user finances
│   │   ├── migrations/
│   │   ├── __init__.py     # Package initialisation
│   │   ├── admin.py        # Admin settings for package
│   │   ├── apps.py         # Package settings
│   │   ├── models.py       # Package models
│   │   ├── tests.py        # Testing functions for package
│   │   ├── permitions.py   # Custom prmitions
│   │   ├── serialisers.py  # Serialisers for db.models to json convert.
│   │   ├── urls.py         # Package routing manager
│   │   ├── utils.py        # TASK 2: fibonacci function
│   │   └── views.py        # Package controllers
│   │
│   └── manage.py           # Django-admin tasts executor
│ 
├── requirements.txt        # Environment files
├── Pipfile                 # 
├── Pipfile.lock            # 
├── .env                    # File with all important project variables
├── .dockerignore           # Docker files
├── docker-compose.yaml     # 
├── Dockerfile              # 
└── README.md               # Project description
```

## Run project
Project is fully wrapped in one docker-compose file. No virtual enviroments need to be created!
```
git clone https://github.com/Genvekt/akvelon_python_internship_3_Evgenia_Kivotova
cd akvelon_python_internship_3_Evgenia_Kivotova
```
Change PROJECT_ROOT in .env file to the absolute path to akvelon_python_internship_3_Evgenia_Kivotova folder.
```
docker network create FinanceNet
docker-compose up -d
```

## Test API
By default, swagger web interface is available at <a>localhost:8000</a>.
Application requires tocken authentification for performing API calls. 
It is needed to separate sensitive user information from outsiders.

### Tocken Creation

To create tocken, we need to register user.
Endpoint for user creation:
```
/auth/users/
```

After that user may login to reseice tocken.
Endpoint for user login. Returns auth tocken!
```
/auth/token/login/
```

### How to use tocken
Tocken may be passed into api-key field by pressing swagger Authenticate button.
Valid format for api-key field is `Tocken <TOKEN>`.

Token may be also used in curl:
```
curl -X GET --header 'Accept: application/json' --header 'Authorization: Token <TOKEN>' 'http://localhost:8000/api/finance_manager/transactions?date=2011-01-30'
```

### API important endpoints
- Endpoint for listing all users.

```
http://localhost:8000/api/finance_manager/users/
```

- Endpoint for listing and modifying one user information. 
  Everyone can view, only owner modify.

```
http://localhost:8000/api/finance_manager/user/<int:id>
```

- Endpoint for transaction creation. Automatically assigned to token owner.

```
http://localhost:8000/api/finance_manager/transaction/create
```

- Endpoint for listing and modifying one transaction information. Only owner has access.

```
http://localhost:8000/api/finance_manager/transaction/<int:id>
```

- Endpoint for listing all user transactions.
    
    Avaivable UTM parameters:

        - date = YYYY-MM-DD : Select transactions, made in specific date.
        - type = income / outcome : Select transactions based on amount sign.
        - sort_date = True / true /  : Sort result by date
        - sort_amount = True / true / : Sort result by amount

    If both sort_date and sort_amount are provided, 
    sort by date is performed first.
```
http://localhost:8000/api/finance_manager/transactions
```

- Endpoint for grouping user transactions by date.

    Avaivable UTM parameters:

        - start = YYYY-MM-DD : starting date of range. Default is 1000-01-01
        - end = YYYY-MM-DD: ending date of range. Default is 9999-12-31

```
http://localhost:8000/api/finance_manager/transaction/grouped
```

- Endpoint for fibonacci function test

```
http://localhost:8000/api/finance_manager/fibonacci/<int:n>
```


## Stop project and clear all files
```
docker-compose down -v --rmi all
```
