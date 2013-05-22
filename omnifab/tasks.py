from fabric.api import env, lcd, local, task

@task
def vagrant(vagrant_dir):
    """Run subsequent tasks on a vagrant machine

    Use as follows:

        fab vagrant:/path/to/vagrant_dir task1 task2
    """
    with lcd(vagrant_dir):
        result = local('vagrant ssh-config', capture=True)

    params = {}
    good_to_go = False
    for line in result.split('\n'):
        if line.startswith('Host'):
            good_to_go = True
        if good_to_go:
            k,v = line.strip().split(None,1)
            params[k] = v

    # change from the default user to 'vagrant'
    env.user = params["User"]
    # connect to the port-forwarded ssh
    env.hosts = ["%s:%s" % (params["HostName"], params["Port"])]
    # use vagrant ssh key
    env.key_filename = params["IdentityFile"].strip('"')

@task
def shell():
    """Runs an interactive shell"""
    import fabric.api as fab
    assert fab # Silence pyflakes
    banner = "Interactive fabric shell. Use 'fab' to access fabric " + \
    "such as fab.run('ls')"
    try:
        from IPython import embed
    except ImportError:
        # We don't have ipython, do a regular shell
        import code
        code.interact(banner, local=locals())
    else:
        embed(banner1=banner)
