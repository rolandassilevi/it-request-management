## Architecture métier de ITRequest
it-request-management/
│
├── config/                    # Configuration globale Django
│
├── apps/
│   │
│   ├── accounts/              # Utilisateurs / authentification
│   ├── organizations/         # Structures + contacts
│   ├── catalog/               # Catégories + produits
│   ├── requests/              # Demandes + lignes
│   ├── quotations/            # Cotations + lignes
│   └── dashboard/             # KPI / tableau de bord
│
├── templates/                 # Templates communs
├── static/                    # CSS, JS, images
├── documentation/
├── manage.py
├── requirements.txt
├── .env
└── .env.example

## Interfaces
Interface                         Application Django

Connexion                  →      accounts
Dashboard                  →      dashboard
Liste structures           →      organizations
Fiche structure            →      organizations
Catalogue produits         →      catalog
Nouvelle demande           →      requests
Détail demande             →      requests
Création cotation          →      quotations
Liste cotations            →      quotations

## Modèle relationnel
Organization
     │
     ├────< Contact
     │
     └────< Request
              │
              ├────< RequestItem >──── Product >──── Category
              │
              └────< Quotation
                        │
                        └────< QuotationItem

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

main
 │
 ● 6a0d989  Django initial
 │
 └── develop
      │
      ● 0dd2625  Git evidence
      │
      ● xxxxxxx  Django + PostgreSQL
      ↑
     HEAD

*******

ITRequest
│
├── Python 3.13.3
├── environnement virtuel .venv
├── Django 6.1.1
├── Psycopg 3.3.6
├── PostgreSQL 17.5
│   ├── itrequest_db
│   └── itrequest_app
├── gestion sécurisée .env
├── migrations Django
├── Git
│   ├── main
│   └── develop
└── documentation par preuves

*******

main
│
● 6a0d989  chore: initialize Django project
│
└── develop
    │
    ● 0dd2625  docs: add Git staging validation evidence
    │
    ● f5c97d9  feat: configure Django with PostgreSQL
    ↑
   HEAD

*******

Django 6.1.1
     ↓
python-dotenv
     ↓
.env
     ↓
Django ORM
     ↓
Psycopg 3.3.6
     ↓
PostgreSQL 17.5
     ↓
itrequest_db
     ↓
10 tables Django

*******

## Créations des apps
P04-01  Corriger/valider requirements.txt
P04-02  Créer l'arborescence apps/
P04-03  Créer l'app organizations
P04-04  Comprendre les fichiers générés par startapp
P04-05  Enregistrer l'app dans INSTALLED_APPS
P04-06  Concevoir Organization
P04-07  Concevoir Contact
P04-08  Créer les modèles Python
P04-09  python manage.py check
P04-10  makemigrations
P04-11  inspecter le SQL avec sqlmigrate
P04-12  migrate
P04-13  inspecter les nouvelles tables PostgreSQL
P04-14  vérifier PK/FK/contraintes
P04-15  créer des données via Django shell
P04-16  interroger les mêmes données en SQL
P04-17  enregistrer les modèles dans Django Admin
P04-18  créer le superutilisateur
P04-19  tester l'interface /admin
P04-20  documentation + Git

*******

apps\
└── __init__.py

Le fichier __init__.py permet notamment à Python de traiter apps comme un package Python explicite.

*******

organizations\
├── migrations\
│   └── __init__.py
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py

*******

config/
    = le PROJET Django
    = configuration globale

apps/organizations/
    = une APPLICATION Django
    = une fonction métier de la plateforme

## Passer d'un besoin métier à un modèle relationnel, puis seulement ensuite au code Django
Organization
     1
     │
     │ possède
     │
     N
   Contact

* Relation SQL
organizations_organization
           ↑
           │ organization_id (FK)
           │
organizations_contact

*******

## Modèle Organization
Organization
─────────────────────────────────
id                  PK
name                VARCHAR
organization_type   VARCHAR
registration_number VARCHAR, nullable
address             VARCHAR
city                VARCHAR
country             VARCHAR
phone               VARCHAR
email               VARCHAR
website             URL, nullable
description         TEXT
is_active            BOOLEAN
created_at          TIMESTAMP
updated_at          TIMESTAMP

* Les types de structures seront contrôlés
PME
ONG
Institution
École
Entreprise
Association
Autre

## Modèle Contact
Contact
─────────────────────────────────
id              PK
organization_id FK → Organization
first_name      VARCHAR
last_name       VARCHAR
job_title       VARCHAR
email           VARCHAR
phone           VARCHAR
is_primary      BOOLEAN
is_active       BOOLEAN
created_at      TIMESTAMP
updated_at      TIMESTAMP


Organization
────────────
id PK
name
...
    │
    │ 1:N
    ▼
Contact
────────────
id PK
organization_id FK
first_name
last_name
...

Exemple :
ONG Avenir
│
├── Marie Dupont
│   Contact principal
│
├── Jean Mensah
│   Responsable administratif
│
└── Ama Lawson
    Responsable achats

## De Python/Django vers le schéma SQL
Python → Django ORM → migration → SQL PostgreSQL → tables

organizations_organization
    id                  PK
    name
    organization_type
    registration_number
    address
    city
    country
    phone
    email
    website
    description
    is_active
    created_at
    updated_at

organizations_contact
    id                  PK
    organization_id     FK
    first_name
    last_name
    job_title
    email
    phone
    is_primary
    is_active
    created_at
    updated_at


*******

organizations_organization
          id PK
            │
            │ 1
            │
            │ N
            ▼
organizations_contact
     organization_id FK

## Migration

```python
python manage.py makemigrations organizations
python manage.py showmigrations organizations

```

organizations
 [ ] 0001_initial

 models.py
    ↓
makemigrations
    ↓
0001_initial.py
    ↓
PAS ENCORE PostgreSQL

* Demander à Django le SQL prévu

```python
python manage.py sqlmigrate organizations 0001

```

Django
models.Model
        ↓
Migration
CreateModel
        ↓
PostgreSQL
CREATE TABLE

Django
ForeignKey
        ↓
PostgreSQL
FOREIGN KEY

*******

| Django | PostgreSQL |
|---|---|
| `CharField(max_length=150)` | `varchar(150)` |
| `TextField` | `text` |
| `BooleanField` | `boolean` |
| `DateTimeField` | `timestamp with time zone` |
| clé primaire automatique | `bigint ... GENERATED BY DEFAULT AS IDENTITY` |
| `ForeignKey` | colonne `organization_id` + contrainte `FOREIGN KEY` |

Les champs définis avec blank=True sont générés avec NOT NULL

blank=True
    → validation Django/formulaire
    → chaîne vide autorisée

null=True
    → stockage SQL
    → NULL autorisé

*******

Besoin métier
     ↓
classes Python
     ↓
Django models
     ↓
makemigrations
     ↓
0001_initial.py
     ↓
sqlmigrate
     ↓
SQL PostgreSQL
     ↓
migrate
     ↓
tables réelles
     ↓
PK + FK + contraintes

*******

PYTHON / DJANGO                       SQL / POSTGRESQL

Organization.objects.create()  →     INSERT INTO ...

Contact.objects.create()       →     INSERT INTO ...

Organization.objects.all()     →     SELECT ...

organization.contacts.all()    →     SELECT ... WHERE organization_id = ...

ForeignKey                     →     FOREIGN KEY

organization.id                →     PRIMARY KEY

organization=organization      →     organization_id

ORM                            →     SQL

*******

## Architecture fonctionnelle
Utilisateur
    │
    ▼
Django Admin
    │
    ▼
OrganizationAdmin / ContactAdmin
    │
    ▼
Django ORM
    │
    ├── Organization
    │
    └── Contact
          │
          │ ForeignKey
          ▼
      Organization
    │
    ▼
psycopg
    │
    ▼
PostgreSQL
    │
    ├── organizations_organization
    └── organizations_contact

*******
Tests dans les 2 sens:
Django Shell ──CREATE──► PostgreSQL ──READ──► Django Admin

Django Admin ──CREATE──► PostgreSQL ──SELECT──► psql

*******

P01  Environnement Python/Django             ✓
P02  Git / branche develop                   ✓
P03  PostgreSQL + Django                     ✓
P04  Organizations + Contacts                ✓
      ├── modèles                            ✓
      ├── ForeignKey                         ✓
      ├── migrations                         ✓
      ├── PostgreSQL                         ✓
      ├── ORM                                ✓
      ├── données réelles                    ✓
      ├── Django Admin                       ✓
      └── CRUD Django → PostgreSQL            ✓

*******

CATEGORY
--------
id
name
code
description
is_active
created_at
updated_at

        1
        │
        │ contains
        │
        N

PRODUCT
-------
id
category_id
name
sku
brand
model
description
unit_price
is_active
created_at
updated_at

*******

name  = apps.catalog
        ↑ chemin Python complet

label = catalog
        ↑ identifiant court Django

*******

product.category
      ↓
« Quelle est la catégorie de ce produit ? »

category.products.all()
      ↓
« Quels sont tous les produits de cette catégorie ? »

*******

unit_price = models.DecimalField(
    max_digits=12,
    decimal_places=2,
)

decimal_places=2 réserve deux chiffres après la virgule.
max_digits=12 signifie 12 chiffres maximum au total, et non 12 chiffres avant la virgule.

9999999999.99
│          │
10 chiffres 2 chiffres
             décimaux

= 12 chiffres au total

*******

Organization
     │
     ├── Contact
     │
     └── Request
            │
            └── RequestItem
                    │
                    └── Product
                           │
                           └── Category

