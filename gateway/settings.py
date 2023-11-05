import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic import BaseSettings

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO
<<<<<<< HEAD
    # Variables for the database
    db_host: str = "localhost"
    db_port: int = 5434
    db_user: str = "gateway"
    db_pass: str = "gateway"
    db_base: str = "gateway"
    db_echo: bool = False
=======
>>>>>>> 1165b02eb3d15a3130786787bdc62bf724d0d4d1

    # Gestao
    gestao_host: str = "http://localhost:8001"

    class Config:
        env_file = ".env"
        env_prefix = ""
        env_file_encoding = "utf-8"


settings = Settings()
