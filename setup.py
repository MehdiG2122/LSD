from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='LSDapi',
    version='0.0.3',
    description='Yahoo Finance live stock data',
    long_description_content_type='text/markdown',
    long_description=open('README.txt').read(),
    url='',
    author='Mehdi Ghaouti',
    author_email='ghaouti.mehdi@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='yahoo finance stocks',
    packages=find_packages(),
    install_requires=['requests',
                      'bs4']
)
