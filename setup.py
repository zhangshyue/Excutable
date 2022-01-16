from setuptools import setup
setup(
    name='list_file',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'list_file=list_file:extract'
        ]
    }
)