from fastapi import FastAPI

app = FastAPI(title="Consensus API", version="0.1.0")


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Point de contrôle de santé de l'API."""
    return {"status": "ok"}
