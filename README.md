# Consensus 🗳️

**Consensus** est une plateforme collaborative de vote et de suivi des prix du carburant.

---

## Stack technique

| Couche      | Technologie                          |
|-------------|--------------------------------------|
| Backend     | FastAPI · SQLAlchemy · Alembic       |
| Frontend    | Reflex (Python full-stack)           |
| Base de données | PostgreSQL 16                    |
| Dépendances | uv (Astral)                          |
| Qualité code | Ruff (lint + format)                |
| Conteneurs  | Docker · Docker Compose              |

---

## Lancement rapide (Docker)

### Prérequis

- [Docker](https://docs.docker.com/get-docker/) ≥ 24
- [Docker Compose](https://docs.docker.com/compose/) ≥ 2

### Démarrer l'application

```bash
git clone https://github.com/alexandrecharvier95/consensus.git
cd consensus
docker compose up --build
```

L'application sera disponible sur :
- **Frontend** : http://localhost:3000
- **Backend API** : http://localhost:8000
- **Documentation API** : http://localhost:8000/docs

Pour arrêter :
```bash
docker compose down
```

Pour supprimer également les volumes (données PostgreSQL) :
```bash
docker compose down -v
```

---

## Développement local (sans Docker)

### Prérequis

- Python ≥ 3.12
- [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- PostgreSQL 16 en local (ou via Docker : `docker compose up db`)

### Backend

```bash
cd back
uv sync
uv run uvicorn app.main:app --reload
```

### Frontend

```bash
cd front
uv sync
uv run reflex run
```

---

## Migrations de base de données

```bash
cd back

# Créer une nouvelle migration (autogenerate)
uv run alembic revision --autogenerate -m "description"

# Appliquer les migrations
uv run alembic upgrade head

# Annuler la dernière migration
uv run alembic downgrade -1
```

---

## Qualité de code

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Vérification du format (sans modification)
uv run ruff format --check .
```

---

## Variables d'environnement

| Variable      | Description                        | Défaut       |
|---------------|------------------------------------|--------------|
| `DB_HOST`     | Hôte PostgreSQL                    | `localhost`  |
| `DB_PORT`     | Port PostgreSQL                    | `5432`       |
| `DB_USER`     | Utilisateur PostgreSQL             | `postgres`   |
| `DB_PASSWORD` | Mot de passe PostgreSQL            | `postgres`   |
| `DB_NAME`     | Nom de la base de données          | `consensus`  |
| `APP_ENV`     | Environnement applicatif           | `development`|

---

## Licence

Ce projet est propriétaire. Voir le fichier [LICENSE](./LICENSE) pour plus de détails.
