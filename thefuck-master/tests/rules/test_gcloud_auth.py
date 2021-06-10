from thefuck.rules.gcloud_auth import match, get_new_command
from thefuck.types import Command


def test_match():
    response1 = """
    ERROR: (gcloud.pubsub.subscriptions.list) You do not currently have an active account selected.
"""
    assert match(Command('gcloud pubsub subscriptions list', response1))

    response2 = """
    ERROR: (gcloud.ai-platform) Command name argument expected.
"""
    assert not match(Command('gcloud ai-platform', response2))


def test_get_new_command():
    assert get_new_command(Command('gcloud pubsub subscriptions list', '')) == 'gcloud auth login && gcloud pubsub subscriptions list'
    assert get_new_command(Command('gcloud projects describe the-fuck', '')) == 'gcloud auth login && gcloud projects describe the-fuck'
