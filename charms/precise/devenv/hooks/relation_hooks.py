import os


def pq_relation_changed():
    os.system('relation-set database=test')

    host = os.popen('relation-get host').read().strip()
    user = os.popen('relation-get user').read().strip()
    database = os.popen('relation-get database').read().strip()
    password = os.popen('relation-get password').read().strip()
    with open('mongo.conf', 'w') as mfile:
        mfile.write('host=%s\n' % host)
        mfile.write('user=%s\n' % user)
        mfile.write('database=%s\n' % database)
        mfile.write('password=%s\n' % password)

    print "Done!"


def mongo_relation_changed():
    host = os.popen('relation-get hostname').read().strip()
    port = os.popen('relation-get port').read().strip()
    with open('mongo.conf', 'w') as mfile:
        mfile.write('host=%s\n' % host)
        mfile.write('port=%s\n' % port)

    print "Done!"

if __name__ == '__main__':
    hooks = {
            'mongo-relation-changed': mongo_relation_changed,
            'pq-relation-changed': pq_relation_changed,
            }

    hook_name = os.path.basename(sys.argv[0])
    op = hooks.get(hook_name, None)
    if not op is None:
        op()
