from setuptools import setup, find_packages

setup(
    name='TornadoHelloApp',
    version='0.1',
    escription='An example of installable tornado app',
    author='evemorgen',
    url='',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['hellotornado = tornado_app.tornado_helloworld:main', ], },
    install_requires=[
        'tornado==4.4'
    ]
)
