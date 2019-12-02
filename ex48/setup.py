try:
    from setuptools import setup
except ImportError:
    from distutils.code import setup

config = {
    'description': 'My Project',
    'author': 'Jackson Baker',
    'url': 'url',
    'download_url': 'download_url',
    'author_email': 'jacksonbaker323@Gmail.com',
    'version': '0.1',
    'install_requires':['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)