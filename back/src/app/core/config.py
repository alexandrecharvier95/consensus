import os


def _require(name: str) -> str:
    """Retourne la valeur d'une variable d'environnement obligatoire."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"La variable d'environnement '{name}' est requise mais non définie."
        )
    return value


_driver = "postgresql+psycopg"
_user = os.getenv("DB_USER", "postgres")
_pwd = _require("DB_PASSWORD") if os.getenv("APP_ENV", "development") != "test" else os.getenv("DB_PASSWORD", "test")
_host = os.getenv("DB_HOST", "localhost")
_port = os.getenv("DB_PORT", "5432")
_name = os.getenv("DB_NAME", "consensus")

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    f"{_driver}://{_user}:{_pwd}@{_host}:{_port}/{_name}",
)
APP_ENV: str = os.getenv("APP_ENV", "development")
