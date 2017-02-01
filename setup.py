from setuptools import setup

setup(
    name='AngryBirds',
    version='1.0',
    install_requires=[
        'tweepy==3.5.0',
        'requests==2.13.0',
        'click==6.7',
        'pyaml==16.12.2'
    ],
    entry_points='''
        [console_scripts]
        ab=angrybirds.cli:main
    ''',
)
