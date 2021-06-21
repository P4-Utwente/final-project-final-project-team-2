import re

from thefuck.utils import for_app
from thefuck.specific.sudo import sudo_support

@for_app('rmdir')


@sudo_support
def match(command):
    return ('rmdir: failed to remove' in command.output.lower() and "directory not empty" in command.output.lower())

@sudo_support
def get_new_command(command):
	return re.sub('rmdir', 'rmdir -r', command.script)
