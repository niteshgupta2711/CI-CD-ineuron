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
       version='0.0.6',
       description='housing project',
       author=AUTHOR_NAME,
       author_email=AUTHOR_EMAIL,
       packages=find_packages(),   #['housing'], # find packages is a function that finds all the folders with __init__ to identify it as package
       install_requires=get_requirements())

       # -e . will  install all the folders with __init__.py files