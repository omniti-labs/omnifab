# Omnifab - Library of useful helper functions for fabric

This library contains some helper functions that we have found useful while
working with fabric.

The library currently consists of two modules:

 * util - a collection of functions for use in your fabfiles
 * tasks - self contained tasks to help with using fabric

## Tasks module

To use this module, add the following to the top of your fabfile:

    from omnifab import tasks

And you will see some new tasks in the list when you run fab -l:

 * tasks.vagrant - Allows you to simply run tasks against a vagrant VM
 * tasks.shell - A simple interactive shell for testing out fabric commands

### Vagrant task

The vagrant task lets you quickly apply a fabfile to a vagrant vm by including
it as the first task in the list. You specify the path to the vagrant project
as the first parameter. For example:

    fab tasks.vagrant:~/vagrant/myvm task1 task2

This task lets you quickly test out a fabfile without needing to modify it or
manually specify the hostname/port/username/key for vagrant.

## Util module

This contains a collection of helper functions for use in your fabric tasks:

 * test - run a bash test
 * runs_ok - quick wrapper around a shell command, return True if the command
   returns successfully.
 * mkdir - Ensure a directory exists, and do nothing if it does
 * get_homedir_location - guesses where user home directories are stored based
   on a heuristic.
 * git_remote - ensure a given git checkout has a remote set up
