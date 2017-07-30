from setuptools import setup

setup(
    name='TornadoHelloApp',
    version='0.1',
    escription='An example of installable tornado app',
    author='evemorgen',
    url='',
    license='MIT',
    packages=['tornado_app'],
    entry_points={'console_scripts': ['hellotornado = tornado_app.tornado_helloworld', ], },
)
