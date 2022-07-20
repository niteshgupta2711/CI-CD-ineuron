from setuptools import setup,find_packages
AUTHOR_NAME="NITESH kumar gupta"
AUTHOR_EMAIL='guptanitesh2711@gmail.com'
long_description='this is a first fsds nov batch ml project'

HYPHEN_E_DOT='-e .'
setup(name='housing',
       version='0.0.1',
       description='housing project',
       author=AUTHOR_NAME,
       author_email=AUTHOR_EMAIL,
       packages=['housing'],
       requirements_list=['numpy'])