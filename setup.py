from setuptools import setup, find_packages

setup(
    name='wordscramble',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Cython',
    ],
    entry_points='''
    [console_scripts]
    wordscramble=bin.wordscramble:main
    ''',
)
