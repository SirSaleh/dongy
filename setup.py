import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'readme.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dongycosts',
    version='1.0',
    packages=['dongycosts'],
    include_package_data=True,
    license='GPL V2.',  # example license
    description='A simple Django app to calculate shared costs.',
    long_description=README,
    url='https://www.github.com/sirsaleh/dongy',
    author='SirSaleh',
    author_email='animatorsaleh@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL V2',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)