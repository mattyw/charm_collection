set -ev
juju bootstrap
juju deploy mongodb
juju deploy mysql
juju deploy --repository=charms --constraints "mem=8G" local:precise/devenv
juju add-relation mongodb devenv
juju add-relation mysql devenv

#Can't do postgres yet becuase of bug lp:1172895
#juju deploy postgresql
#juju add-relation postgresql devenv
juju debug-log
