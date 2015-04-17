# coding: utf-8
import sublime

VERSION = int(sublime.version())
if VERSION > 3000:
    from JoomlaPack.lib.helpers import show_message
    from JoomlaPack.lib.helpers import get_settings
    from JoomlaPack.lib.helpers import get_project_root
    from JoomlaPack.lib.helpers import get_templates
    from JoomlaPack.lib.helpers import pluralize
else:
    from lib.helpers import show_message
    from lib.helpers import get_settings
    from lib.helpers import get_project_root
    from lib.helpers import get_templates
    from lib.helpers import pluralize
    from lib.project import Project

__all__ = [
    'show_message',
    'get_settings',
    'get_project_root',
    'get_templates',
    'pluralize',
    'Project'
]
