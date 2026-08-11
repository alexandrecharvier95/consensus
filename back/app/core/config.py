import os

_driver = "postgresql+psycopg"
_user = os.getenv("DB_USER", "postgres")
_pwd = os.getenv("DB_PASSWORD", "postgres")
_host = os.getenv("DB_HOST", "localhost")
_port = os.getenv("DB_PORT", "5432")
_name = os.getenv("DB_NAME", "consensus")

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    f"{_driver}://{_user}:{_pwd}@{_host}:{_port}/{_name}",
)
APP_ENV: str = os.getenv("APP_ENV", "development")
