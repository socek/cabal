# flake8: noqa
from importlib import import_module
from pkgutil import walk_packages

from colorama import Fore
from colorama import Style
from colorama import init
from sapp.plugins.sqlalchemy.alembic import AlembicScript

# import or define all models here to ensure they are attached to the
# SqlTable.metadata prior to any initialization routines
from cabal import application
from cabal.app.db import SqlTable


def search(parent, name):
    tables = []
    print("Searching for all tables")
    for module in walk_packages([parent], f"{parent}."):
        try:
            package = import_module(module.name)
        except Exception:
            print(f"{Fore.RED}[ERRO]{Style.RESET_ALL} Module error: {module.name}")
            continue
        intro = False
        for elementname in dir(package):
            try:
                element = getattr(package, elementname)
                if issubclass(element, SqlTable) and element != SqlTable:
                    if not intro:
                        print(f"{Fore.GREEN}[ OK ]{Style.RESET_ALL} Module found: {module.name}")
                        intro = True
                    print(f"\tFound: {elementname}")
                    tables.append(f"{module.name}:{elementname}")
            except TypeError:
                pass
    print(f" >>> Found {len(tables)} tables\n")


init()
search("cabal", "tables")
AlembicScript(application, SqlTable, "dbsession").run()
