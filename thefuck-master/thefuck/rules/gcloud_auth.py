def match(command):
    return ('gcloud' in command.script and 'You do not currently have an active account selected' in command.output)


def get_new_command(command):

    return 'gcloud auth login && {}'.format(command.script)
