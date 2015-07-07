from setuptools import setup
from brokerc import _version

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='brokerc',
      #version='0.0.1',
      version=_version.__version__,
      description='brokerc',
      #long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 3.4',
      ],
      keywords='brokerc',
      url='https://github.com/flyingcoconut/brokerc',
      author='Patrick Charron',
      author_email='patrick.charron.pc@gmail.com',
      license='GPL v3',
      packages=['bin', 'brokerc'],
      scripts=['bin/brokerc'],
      include_package_data=True,
      zip_safe=False)


