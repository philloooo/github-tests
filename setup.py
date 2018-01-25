from distutils.core import setup
from subprocess import check_output


def get_version():
    try:
        tag = check_output(['git', 'describe',  '--tags', '--abbrev=0'])
        return tag.strip('\n')
    except:
        # if somehow you get the repo not from git,
        # hardcode default minor version
        return '1.2.0'

_version = get_version()

setup(
  name = 'pyttest',
  packages = ['pyttest'], # this must be the same as the name above
  version = _version,
  description = 'A random test lib',
  author = 'Phillis',
  author_email = 'phillis.test@gmail.com',
  url = 'https://github.com/philloooo/pyttest', # use the URL to the github repo
  download_url = 'https://github.com/philloooo/pyttest/archive/{}.tar.gz'.format(_version),
  keywords = ['testing'], # arbitrary keywords
  classifiers = [],
)
