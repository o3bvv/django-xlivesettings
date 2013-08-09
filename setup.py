import os
from setuptools import setup, find_packages

VERSION = (1, 0, 0)

# Dynamically calculate the version based on VERSION tuple
if len(VERSION)>2 and VERSION[2] is not None:
    str_version = "%d.%d_%s" % VERSION[:3]
else:
    str_version = "%d.%d" % VERSION[:2]

version= str_version

install_requires = [
    "django-keyedcache>=1.4-6",
]

setup(
    name = "django-xlivesettings",
    version = version,
    description = "xlivesettings",
    long_description =
    """
    Django-xLivesettings is a fork of Django-Livesettings, which is a project split from the Satchmo Project.
    It provides the ability to configure settings via an admin interface, rather than by editing "settings.py".
    """,
    author = "Alexander Oblovatniy",
    author_email = "oblovatniy@gmail.com",
    url = "https://github.com/oblalex/django-xlivesettings/",
    license = "New BSD License",
    platforms = ["any"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django"],
    packages = find_packages(),
    include_package_data = True,
    install_requires=install_requires,
)
