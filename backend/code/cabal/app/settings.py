from decouple import config

from cabal.app.logging import logging
from cabal.app.meta import version


def default():
    settings = {
        "project_name": "Cabal",
        "version": version,
        "git_sha": config("COMMIT_SHA"),
        "git_branch": config("COMMIT_BRANCH"),
    }
    logging(settings)
    return settings


def webapp():
    settings = default()
    return settings
