# ITRequest

Plateforme Web de gestion des demandes et cotations de matériels informatiques.

## Objectif

ITRequest permet de centraliser et suivre les demandes de matériels informatiques provenant de différentes structures clientes : PME, ONG, institutions, écoles, entreprises et associations.

La plateforme permettra progressivement de :

- gérer les structures clientes et leurs contacts ;
- gérer un catalogue de matériels informatiques ;
- enregistrer les demandes de matériels ;
- gérer plusieurs lignes de produits par demande ;
- préparer des cotations ;
- suivre le statut des demandes et cotations ;
- afficher des indicateurs dans un tableau de bord ;
- gérer l'authentification et les autorisations.

## Stack technique

- Python 3.13
- Django 6.1
- PostgreSQL 17
- HTML
- CSS
- JavaScript
- Bootstrap
- Git / GitHub
- Docker

## Architecture cible

```text
Navigateur Web
      |
      | HTTP / HTTPS
      v
Django / Python
      |
      | Django ORM / SQL
      v
PostgreSQL