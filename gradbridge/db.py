from pymongo import MongoClient
from flask import current_app

_client = None


def get_client():
    global _client
    if _client is None:
        uri = current_app.config.get("MONGO_URI")
        if not uri:
            raise RuntimeError("MONGO_URI is not set in environment variables.")
        _client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    return _client


def get_db():
    db_name = current_app.config.get("MONGO_DB_NAME", "gradbridge")
    return get_client()[db_name]


def ping_db():
    get_client().admin.command("ping")
    return True