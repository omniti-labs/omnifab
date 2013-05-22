from fabric.api import cd, hide, run, settings

def test(test):
    """Runs a bash test without outputting any warnings"""
    return runs_ok("[[ %s ]]" % test)

def runs_ok(*args):
    """Run a command and test its exit status"""
    with settings(hide('warnings', 'stdout', 'stderr'), warn_only=True):
        return run(*args).return_code == 0

def mkdir(d):
    """Ensures a given directory exists"""
    if not test("-d %s" % d):
        run("mkdir -p %s" % d)

def get_homedir_location():
    """Guess the location of home directories on a system"""
    location = '/home'
    with settings(hide('warnings', 'stdout', 'stderr'), warn_only=True):
        # Currently we naively check to see if other common locations for home
        # dirs exist, and if they do, assume that is where home dirs are
        # really stored. We could probably do some more checks here.
        if test("-d /Users"):
            location = "/Users" # Mac
        elif test("-d /export/home"):
            location = "/export/home" # Solaris
    return location

def git_remote(dirname, name, url):
    """Ensures that a given git checkout has the specified remote set up"""
    with cd(dirname):
        remote_info = run("git remote -v | grep %s" % name)
        if remote_info:
            # Remote is present
            current_url = remote_info.split()[1]
            if current_url != url:
                # Remote is present, but the URL needs changing
                run("git remote set-url %s %s" % (name, url))
        else:
            # Remote isn't present, we should add it
            run("git remote add %s %s" % (name, url))
