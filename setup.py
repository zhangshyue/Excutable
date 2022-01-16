from setuptools import setup
setup(
    name='list_file',
    version='0.0.1',
    author="Shiyue Zhang",
     author_email="zhangshiyuez@gmail.com",
     description="A package for listing file names in directory",
     url="https://github.com/zhangshyue/listFile",
    entry_points={
        'console_scripts': [
            'list_file=list_file:extract'
        ]
    }
)