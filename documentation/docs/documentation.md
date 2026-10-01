## Postgre database role

PostgreSQL 17.5
│
├── rôle administrateur
│   └── postgres
│
├── rôle applicatif
│   └── itrequest_app
│       ├── LOGIN : oui
│       └── superuser : non
│
└── base applicative
    └── itrequest_db
        ├── Owner : itrequest_app
        ├── Encoding : UTF8
        ├── Schema courant : public
        └── Tables : 


## Pilote PostgreSQL

Django
   │
   │ Django ORM
   ↓
psycopg  <------------ Pilote PostgreSQL
   │
   │ protocole PostgreSQL
   ↓
PostgreSQL 17.5

## Protection du secret 
Contrôle de sécurité

.env
│
├── DB_NAME
├── DB_USER
├── DB_PASSWORD   ← SECRET
├── DB_HOST
└── DB_PORT

       X
       │
       │ .gitignore
       ▼

      Git

## Chargement .env dans Django

.env
 ↓
python-dotenv
 ↓
os.environ
 ↓
settings.py
 ↓
Django

*******

Django
  ↓
settings.py
  ↓
variables .env
  ↓
psycopg
  ↓
PostgreSQL
  ↓
itrequest_db

*******
Python 3.13
     ↓
Django 6.1
     ↓
settings.py
     ↓
.env
     ↓
psycopg
     ↓
PostgreSQL 17.5
     ↓
itrequest_db
     ↓
itrequest_app

## Comprendre les migrations
Django connaît les migrations
              ↓
admin        [ ]
auth         [ ]
contenttypes [ ]
sessions     [ ]

             MAIS

PostgreSQL
    ↓
\dt
    ↓
aucune table


[ ] signifie : migration connue de Django mais pas encore appliquée à cette base PostgreSQL.
Après migrate, elles deviendront [X]

*******

AVANT

itrequest_db
└── aucune table


python manage.py migrate
          ↓


APRÈS

itrequest_db
├── auth_user
├── auth_group
├── auth_permission
├── django_admin_log
├── django_content_type
├── django_migrations
├── django_session
└── ...

*******

Fichiers migrations
        ↓
Django
        ↓
SQL
        ↓
PostgreSQL
        ↓
django_migrations
        ↓
historique des migrations appliquées

*******

             ITREQUEST — ENVIRONNEMENT LOCAL

┌──────────────────┐
│ Python 3.13.3    │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Django 6.1.1     │
│ ORM + migrations │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Psycopg 3.3.6    │
└────────┬─────────┘
         ↓
┌──────────────────────────────┐
│ PostgreSQL 17.5              │
│                              │
│ Database : itrequest_db      │
│ User     : itrequest_app     │
└──────────────────────────────┘

Secrets
.env ───────X──────→ Git

Configuration reproductible
.env.example ──────→ Git
requirements.txt ──→ Git

*******

