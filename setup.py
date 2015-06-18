from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='brokerc',
      version='0.0.1',
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
      package_dir = {
          'drivers': 'drivers'
      },
      #install_requires=['redis', 'python3-pika', 'kafka-python', 'pyzmq', 'boto', 'stomp.py', 'paho-mqtt'],
      scripts=['bin/brokerc'],
      include_package_data=True,
      zip_safe=False)


