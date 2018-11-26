from setuptools import setup, find_packages


setup(
    name             = 'dictest',
    version          = '0.1',
    description      = 'It will help you to remember english word',
    long_description = open('README.md').read(),
    author           = 'dsm-helper',
    author_email     = 'dev.moreal@gmail.com',
    url              = 'https://github.com/dsm-helper/dictest',
    download_url     = 'https://',
    install_requires = [],
    packages         = find_packages(exclude = ['docs', 'tests']),
    keywords         = ['word-test', 'study', 'helper'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3.6'
    ]
)