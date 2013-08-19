#!/usr/bin/env python
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

requires = [
    'ansible',
]

setup(
    name='ansible_playbook_wrapper',
    version='0.0.1',
    description='wrapper for ansible-playbook',
    author='Satoshi Ebihara',
    author_email='succhiello@gmail.com',
    url='http://succhiello.net',
    packages=find_packages(),
    install_requires=['ansible'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
            'ansible-playbook-wrapper = ansible_playbook_wrapper:main',
        ],
    }
)
