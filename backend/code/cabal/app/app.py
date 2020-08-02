from sapp.plugins import SettingsPlugin
from sapp.plugins.pyramid.configurator import ConfiguratorWithPyramid
from sapp.plugins.pyramid.plugins import RoutingPlugin
from sapp.plugins.sqlalchemy.plugin import DatabasePlugin

from cabal.webapp.routing import CabalWebappRouting


class CabalConfigurator(ConfiguratorWithPyramid):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin("cabal.app.settings"))
        self.add_plugin(RoutingPlugin(CabalWebappRouting))
        self.add_plugin(DatabasePlugin('dbsession'))


application = CabalConfigurator()
