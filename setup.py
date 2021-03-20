from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='LSDyf',
    version='0.0.1',
    description='Yahoo Finance live stock data',
    long_description=open('README.md').read() + '\n\n' + open('RELEASE.txt').read(),
    url='',
    author='Mehdi Ghaouti',
    author_email='ghaouti.mehdi@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='yahoo finance',
    packages=find_packages(),
    install_requires=['requests',
                      'bs4']
)
