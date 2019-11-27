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
    'packages': ['ex47'],
    'scripts': [],
    'name': 'Exercise 47'
}

setup(**config)
