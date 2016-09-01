from setuptools import setup
from past.builtins import execfile
execfile('lino_algus/setup_info.py')
if __name__ == '__main__':
    setup(**SETUP_INFO)
