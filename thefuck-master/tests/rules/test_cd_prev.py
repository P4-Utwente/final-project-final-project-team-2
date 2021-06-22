from thefuck.rules.cd_prev import match, get_new_command
from thefuck.types import Command


def test_match():
    assert match(Command('cd-', 'Command \'cd-\' not found, did you mean:'))
    assert not match(Command('', ''))


def test_get_new_command():
    assert get_new_command(Command('cd-', '')) == 'cd -'
