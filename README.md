Some simple Juju Charms
===================

[juju.ubuntu.com](http://juju.ubuntu.com)

hellojuju
------------
A minimal "Hello World" charm

helloserver
----------------
Deploys a python webserver with a configurable port

How to deploy
--------------------
Each charm has a corresponding deploy script which bootstraps the env and contains specific information for that deployment
    
    ./deploy_<charmName>/sh

You can tear down the environment using
     
    juju destroy-environment
