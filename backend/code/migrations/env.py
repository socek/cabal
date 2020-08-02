# flake8: noqa
from importlib import import_module
from pkgutil import iter_modules

from colorama import Fore
from colorama import Style
from colorama import init
from sapp.plugins.sqlalchemy.alembic import AlembicScript

# import or define all models here to ensure they are attached to the
# SqlTable.metadata prior to any initialization routines
from cabal import application
from cabal.app.db import SqlTable

init()
mainname = "cabal"
ignore = ["app", "webapp"]
for module in iter_modules(["cabal"]):
    if module.name in ignore:
        continue
    modulepath = f"{mainname}.{module.name}.drivers.tables"
    try:
        import_module(modulepath)
        print(f"{Fore.GREEN}[ OK  ] Module found: {modulepath}{Style.RESET_ALL}")
    except ModuleNotFoundError:
        print(f"{Fore.YELLOW}[FAIL ] Module not found: {modulepath}{Style.RESET_ALL}")
    except SyntaxError:
        print(f"{Fore.RED}[ERROR] Module syntax error: {modulepath}{Style.RESET_ALL}")

AlembicScript(application, SqlTable, "dbsession").run()
