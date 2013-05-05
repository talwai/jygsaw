from distutils.core import setup

setup(
    name='Jygsaw',
    version='0.2.0',
    author='Balkcom\'s Army',
    author_email='jygsaw@cs.dartmouth.edu',
    packages=['jygsaw', 'jygsaw.test'],
    scripts=[],
    url='https://bitbucket.org/haplesshero13/cs98library/',
    license='LICENSE.txt',
    description='Jygsaw graphics library.',
    long_description=open('README.md').read(),
)
