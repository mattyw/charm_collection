set -ev
juju deploy --repository=charms local:precise/devenv
juju debug-log
