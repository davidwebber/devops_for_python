from setuptools import setup

setup(
   name='flask_app',
   version='0.1',
   description='A simple flask application to webify dict_cache',
   author='David Webber',
   author_email='david.webber@gmail.com',
   packages=['flask_app'],  #same as name
   include_package_data=True,
   install_requires=['dict_cache', 'flask'], #external packages as dependencies
   scripts=[]
)
