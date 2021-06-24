'''Rules for apt-get'''
from types import ModuleType
from thefuck.specific.apt import apt_available
from thefuck.utils import memoize, which
from thefuck.shells import shell

try:
    from CommandNotFound import CommandNotFound

    ENABLED_BY_DEFAULT = apt_available

    if isinstance(CommandNotFound, ModuleType):
        # For ubuntu 18.04+
        _get_packages = CommandNotFound.CommandNotFound().get_packages
    else:
        # For older versions
        _get_packages = CommandNotFound().getPackages
except ImportError:
    ENABLED_BY_DEFAULT = False


def _get_executable(command):
    '''-get_executable function'''
    if command.script_parts[0] == 'sudo':
        return command.script_parts[1]
    return command.script_parts[0]


@memoize
def get_package(executable):
    '''get_package function'''
    try:
        packages = _get_packages(executable)
        return packages[0][0]
    except IndexError:
        # IndexError is thrown when no matching package is found
        return None


def match(command):
    '''match function'''
    if 'not found' in command.output or 'not installed' in command.output:
        executable = _get_executable(command)
        return not which(executable) and get_package(executable)
    return False


def get_new_command(command):
    ''''get_new_command function'''
    executable = _get_executable(command)
    name = get_package(executable)
    formatme = shell.and_('sudo apt-get install {}', '{}')
    return formatme.format(name, command.script)
