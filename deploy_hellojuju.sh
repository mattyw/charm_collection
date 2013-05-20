set -ev
juju bootstrap
juju deploy --repository=charms local:precise/hellojuju
juju debug-log
