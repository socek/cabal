from cabal.app.logging import logging


def default():
    settings = {
        "project_name": "Cabal",
    }
    logging(settings)
    return settings


def webapp():
    settings = default()
    return settings
