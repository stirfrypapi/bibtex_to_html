"""
Citation python package configuration.
Raymond Pang <pangr@umich.edu>
"""

from setuptools import setup

setup(
    name='citation',
    version='0.1.0',
    packages=['citation'],
    include_package_data=True,
    install_requires=[
        'arrow==0.15.1',
        'bibtexparser==1.0.1',
        'bs4==0.0.1',
        'Flask==2.3.2',
        'html5validator==0.3.1',
        'pycodestyle==2.5.0',
        'pydocstyle==4.0.1',
        'pylint==2.3.1',
        'pytest==5.1.2',
        'requests==2.22.0',
        'sh==1.12.14',
    ],
)