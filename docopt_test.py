"""Sven.
Usage:
  docopt_test.py hello <name>
  docopt_test.py goodbye <name>
  docopt_test.py page <name> <itemNum> [--allPage=<num>]
  docopt_test.py (-h | --help)
Options:
  -h --help     Show this screen.
"""
from docopt import docopt


def hello(name):
    print('Hello, {0}'.format(name))


def goodbye(name):
    print('Goodbye, {0}'.format(name))

def page(name,item,allpg):
    print('You will extract {0} items from page {1}, and the number of pages is {2}!'.format(name,item,allpg))


if __name__ == '__main__':
    arguments = docopt(__doc__)

    # if an argument called hello was passed, execute the hello logic.
    if arguments['hello']:
        hello(arguments['<name>'])
    elif arguments['page']:
        page(arguments['<name>'],arguments['<itemNum>'],arguments['--allPage'])
    elif arguments['goodbye']:
        goodbye(arguments['<name>'])