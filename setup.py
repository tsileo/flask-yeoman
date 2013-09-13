from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='flask-yeoman',
    version='0.1.0',
    author="Thomas Sileo",
    author_email="thomas.sileo@gmail.com",
    license="MIT",
    keywords="flask yeoman",
    url="https://github.com/tsileo/flask-yeoman/",
    long_description=read('README.rst'),
    py_modules=['flask_yeoman'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
)
