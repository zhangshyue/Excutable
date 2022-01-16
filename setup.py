from setuptools import setup, find_packages
setup(
    name='listFile',
    packages = find_packages(),
    version='0.0.1',
    license='MIT',
    author="Shiyue Zhang",
     author_email="zhangshiyuez@gmail.com",
     description="A package for listing file names in directory",
     url="https://github.com/zhangshyue/listFile",
    entry_points={
        'console_scripts': [
            'list_file=listFile.list_file:extract'
        ]
    }
)