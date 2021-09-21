#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

__doc__ = '''
A Hello world program is usually a program made by computer programmers that are new to a programming languages, 
or to test if the compiler for this language is working correctly. It will simply put the text Hello, World! on 
the screen. One way to do the Hello World program is shown below, in the C programming language.
'''

# zip_safe：用于强制或防 止创建 zip 压缩包。通常你不会想要把包安装为 zip 压缩文件，因为一些工具不支 持压缩文件，而且压缩文件比较难以调试。
setup(
    name = "HelloWorld", 
    version = '0.1.0', 
    packages = find_packages(),
    author = 'phoenix', 
    author_email = 'phoenix@xxx.com',
    description = 'Hello World python rpm',
    long_description = __doc__,
    license = 'GPL',
    url = 'https://simple.wikipedia.org/wiki/Hello_world_program',
    platforms = 'x86-64',
    include_package_data = True,
    install_requires = ['configobj==5.0.6'],
    dependency_links = ['http://mirrors.163.com/pypi/simple'],
    entry_points={
        'console_scripts': [
            'helloworld = HelloWorld.main:main'
        ]
    }
    )

