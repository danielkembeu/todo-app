my_fastapi_app/
├── app/
│   ├── __init__.py
│   ├── main.py                # Point d’entrée FastAPI
│   ├── config.py              # Variables d’env, configs DB
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py         # Engine, SessionLocal SQLModel
│   │   ├── base.py            # SQLModel base imports
│   │   └── migrations/        # Alembic ou outils migrations
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── routes/        # fichiers routeurs par ressource
│   │   │   └── schemas/       # schémas Pydantic si séparés
│   ├── models/
│   │   ├── __init__.py
│   │   └── *.py               # classes SQLModel (table=True)
│   ├── crud/
│   │   ├── __init__.py
│   │   └── *.py               # fonctions CRUD réutilisables
│   ├── services/              # logique métier (facultatif)
│   ├── dependencies.py        # Depends réutilisés
│   └── tests/
│       ├── conftest.py
│       ├── test_*.py
│       └── fixtures.py
├── requirements.txt
├── .env
└── README.md
