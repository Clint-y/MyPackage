from setuptools import setup, find_packages

setup(
    name = 'MyPackage',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    license ='MIT',
    description = 'EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='<your name>',
    author_email='your email>'
    
)