from thefuck.rules.cargo import match, get_new_command
from thefuck.types import Command


def test_match():
    assert match(Command('cargo', 'Command \'cargo\' not found, did you mean:'))
    assert not match(Command('', ''))


def test_get_new_command():
    assert get_new_command(Command('cargo', '')) == 'cargo build'
