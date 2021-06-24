from thefuck.utils import for_app


@for_app('ag')
def match(command):
    """A dummy docstring."""
    return command.output.endswith('run ag with -Q\n')


def get_new_command(command):
    """A dummy docstring."""
    return command.script.replace('ag', 'ag -Q', 1)
