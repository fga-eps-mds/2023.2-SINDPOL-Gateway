from ormar import ModelMeta

from gateway.db.config import database
from gateway.db.meta import meta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta
