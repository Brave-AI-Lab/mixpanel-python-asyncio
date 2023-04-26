from codecs import open
from os import path
import re
from setuptools import setup, find_packages

def read(*paths):
    filename = path.join(path.abspath(path.dirname(__file__)), *paths)
    with open(filename, encoding='utf-8') as f:
        return f.read()

def find_version(*paths):
    contents = read(*paths)
    match = re.search(r'^__version__ = [\'"]([^\'"]+)[\'"]', contents, re.M)
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)

setup(
    name='mixpanel_asyncio',
    version=find_version('mixpanel_asyncio', '__init__.py'),
    description='Unofficial Mixpanel library for Python asyncio',
    long_description=read('README.rst'),
    url='https://github.com/Kylmakalle/mixpanel-python-asyncio',
    author='Sergey Akentev (@Kylmakalle)',
    license='Apache',
    python_requires='>=3.7',
    install_requires=[
        'aiohttp>=3.8.4',
        'aiohttp-retry>=2.8.3'
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='mixpanel analytics asyncio async aio',
    packages=find_packages(),
)
