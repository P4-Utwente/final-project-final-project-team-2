def select_gcloud_auth_command_with_arrows(proc, TIMEOUT):
    proc.sendline(u'gcloud pubsub subscriptions list')
    assert proc.expect([TIMEOUT, u"ERROR: (gcloud.pubsub.subscriptions.list) You do not currently have an active account selected."])

    proc.sendline(u'fuck')
    assert proc.expect([TIMEOUT, u'gcloud auth login && gcloud pubsub subscriptions list'])
