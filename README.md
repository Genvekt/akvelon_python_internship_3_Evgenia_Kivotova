# Finance Management web service
![](https://img.shields.io/github/pipenv/locked/dependency-version/Genvekt/akvelon_python_internship_3_Evgenia_Kivotova/django?color=blue&label=Django) ![](https://img.shields.io/github/pipenv/locked/python-version/Genvekt/akvelon_python_internship_3_Evgenia_Kivotova)

## Project structure
```
.
├── docs/                   # Documentation files
├── finance_site            # Django application
│   │
│   ├── finance_site/       # Configuration package
│   │   ├── __init__.py     # Package initialisation
│   │   ├── asgi.py         # TODO
│   │   ├── settings.py     # Application settings
│   │   ├── urls.py         # Application routing manager
│   │   └── wsgi.py         # TODO 
│   │
│   ├── finance_manager/    # Package for managing user finances
│   │   ├── migrations/
│   │   ├── __init__.py     # Package initialisation
│   │   ├── admin.py        # Admin settings for package
│   │   ├── apps.py         # Package settings
│   │   ├── models.py       # Application routes
│   │   ├── tests.py        # Testing functions
│   │   ├── urls.py         # Package routing manager
│   │   └── views.py        # Package controllers
│   │
│   └── manage.py           # Django-admin tasts executor
├── requirements.txt        # Environment files
├── Pipfile                 # 
├── Pipfile.lock            # 
└── README.md               # Project description
```
