"""
Project management command line tasks.

To see task list run:
$ invoke --complete

To see task help run:
$ invoke -h <task>

"""
from invoke import task

@task
def clean(c, all=False, dist=False):
    """Clean the project directory.

    Clean task always removes build and *.egg-info directories.
    You can specify additional directories to be removed.

    Parameters
    ----------
    all
        Remove all.

    dist
        Remove dist.

    """
    patterns = ['build', '*.egg-info']
    if all:
        patterns.append('dist')
    else:
        if dist:
            patterns.append('dist')
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))

@task
def build(c, egg=False):
    """
    Build the project.

    By default build will create source distribution and wheel 
    binary distribution.

    Build output is stored undr the dist directory.

    Parameters
    ----------
    egg
        Specifying this flag will also create also egg binary
        distribution.

    """
    what = ['sdist', 'bdist_wheel']
    if egg:
        what.append("bdist_egg")
    c.run("python setup.py {}".format(" ".join(what)))
    pass

@task
def test(c,all=False,unit=False,func=False):
    """
    Execute one or more test sites.

    Execute specifined test sites. If no site is specified,
    execute unit tests.

    Parameters
    ----------
    all
        Execute all tests. Ignore all other flags.
    unit
        Execute unit tests.
    func
        Execute functional tests.
    """
    packages = []
    if unit:
        packages.append('tests/unit')
    if func:
        packages.append('tests/func')
    if all:
        packages = ['tests/unit', 'tests/func']
    if not packages:
        packages = ['tests/unit']
    for package in packages:
        c.run("pytest {}".format(package))

