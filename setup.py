from setuptools import setup
import os
from redis_cluster_sessions import __version__

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

packages = ['redis_cluster_sessions']


setup(
    name='django-redis-cluster-sessions',
    version=__version__,
    description= "Redis Cluster Session Backend For Django",
    long_description=read("README.rst"),
    keywords='django, redis, sessions,',
    author='Mikhail Kazan',
    author_email='ospik@@mail.ru',
    url='http://github.com/martinrusev/django-redis-sessions-cluster',
    license='BSD',
    packages=packages,
    zip_safe=False,
    install_requires=['redis>=3.0.0', 'redis-py-cluster>=2.0.0'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    test_suite='tests'
)
