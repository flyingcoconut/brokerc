from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='brokerc',
      version='0.0.1',
      description='brokerc',
      #long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.3',
      ],
      keywords='brokerc',
      url='https://github.com/flyingcoconut/brokerc',
      author='Patrick Charron',
      author_email='patrick.charron.pc@gmail.com',
      license='GPL v3',
      packages=['bin', 'brokerc', 'brokerc/drivers'],
      install_requires=[
      ],
      #entry_points={
      #    'console_scripts': ['mytop=bin:main'],
      #},
      scripts=['bin/brokerc'],
      include_package_data=True,
      zip_safe=False)
