from extras.plugins import PluginConfig
from .version import __version__


class NewpluginConfig(PluginConfig):
    name = 'netbox_newplugin'
    verbose_name = ''
    description = ''
    version = __version__
    author = ''
    author_email = ''
    required_settings = []
    default_settings = {}


config = NewpluginConfig # noqa
