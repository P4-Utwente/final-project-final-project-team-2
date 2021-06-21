# Adds the missing space between the cd command and the target directory
# when trying to cd to the previous directory.
#
# Example:
# > cd-
# Command 'cd-' not found, did you mean:


def match(command):
    return command.script == 'cd-'


def get_new_command(command):
    return 'cd -'
