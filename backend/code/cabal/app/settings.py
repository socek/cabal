from decouple import config

from cabal.app.logging import logging
from cabal.app.meta import version


def default() -> dict:
    settings = {
        "project_name": "Cabal",
        "version": version,
        "git_sha": config("COMMIT_SHA"),
        "git_branch": config("COMMIT_BRANCH"),
    }
    database(settings)
    logging(settings)
    return settings


def database(settings: dict):
    name = config("POSTGRES_DB")
    user = config("POSTGRES_USER")
    password = config("POSTGRES_PASSWORD")
    host = config("POSTGRES_HOST")
    settings["db:dbsession:url"] = f"postgresql://{user}:{password}@{host}:5432/{name}"
    settings["db:dbsession:default_url"] = f"postgresql://{user}:{password}@{host}:5432/postgres"
    settings["db:dbsession:options"] = {"pool_recycle": 3600}
