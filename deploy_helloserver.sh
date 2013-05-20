set -ev
juju bootstrap
juju deploy --repository=charms local:precise/helloserver
juju expose helloserver
juju debug-log
#juju set helloserver port=9000
