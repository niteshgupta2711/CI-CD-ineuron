from setuptools import setup,find_packages
from typing import List
AUTHOR_NAME="NITESH kumar gupta"
AUTHOR_EMAIL='guptanitesh2711@gmail.com'
long_description='this is a first fsds nov batch ml project'
def get_requirements() -> List[str]:
    with open('requirements.txt') as f1:
        l=[line.replace('\n','') for line in f1.readlines()]
    if '-e .' in l:
        l.remove('-e .')
    return l


HYPHEN_E_DOT='-e .'
setup(name='housing',
       version='0.0.1',
       description='housing project',
       author=AUTHOR_NAME,
       author_email=AUTHOR_EMAIL,
       packages=['housing'],
       install_requires=get_requirements())