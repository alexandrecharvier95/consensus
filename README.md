# Consensus 🗳️

**Consensus** est une plateforme collaborative de vote et de suivi des prix du carburant.

## Licence

Ce projet est propriétaire. Voir le fichier [LICENSE](./LICENSE) pour plus de détails.

## Stack technique

| Couche      | Technologie                          |
|-------------|--------------------------------------|
| Backend     | FastAPI · SQLAlchemy · Alembic       |
| Frontend    | Reflex (Python full-stack)           |
| Base de données | PostgreSQL 16                    |
| Dépendances | uv (Astral)                          |
| Qualité code | Ruff (lint + format)                |
| Conteneurs  | Docker · Docker Compose              |


## Déploiement

### Prérequis

- [Docker](https://docs.docker.com/get-docker/) ≥ 24
- [Docker Compose](https://docs.docker.com/compose/) ≥ 2

### Démarrer l'application

```bash
docker compose up --build
```

L'application sera disponible sur :
- **Frontend (GUI)** : http://localhost:3000
- **Backend API** : http://localhost:8000
- **Documentation API** : http://localhost:8000/docs

### Arrêter l'application

```bash
docker compose down
```

Ou pour supprimer également les données PostgreSQL (volumes) :
```bash
docker compose down -v
```

### Variables d'environnement

Voir `docker-compose.yml` pour les variables d'environnement utilisées par l'application. Vous devez créer un fichier `.env` à partir de `.env.example` à la racine du projet pour définir vos propres valeurs.

## Développement

### Gestion des dépendances Python

- [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)

### Migrations de base de données

```bash
cd backend
```

Créer une nouvelle migration (autogénération) :
```bash
uv run alembic revision --autogenerate -m "description"
```

Appliquer les migrations :
```bash
uv run alembic upgrade head
```

Annuler la dernière migration :
```bash
uv run alembic downgrade -1
```

## Qualité du code

Linter :
```bash
uv run ruff check .
```

Formater :
```bash
uv run ruff format .
```

Vérifier le format sans modification :
```bash
uv run ruff format --check .
```
