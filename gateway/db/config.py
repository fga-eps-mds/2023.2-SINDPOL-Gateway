from databases import Database

from gateway.settings import settings

database = Database(str(settings.db_url))
