"""module setup"""

from setuptools import setup

setup(
    name="SMA Data Provider for Sunny Home Manager 2.0",
    version="0.1.0",
    author="Hans Jürgen Böhle",
    author_email="hj@boehle.info",
    url="https://github.com/hjboehle",
    license='MIT',
    description="Data Provider for SMA Sunny Home Manager 2.0",
    long_description="The SMA Sunny Home Manager 2.0 publishes data from the connected " \
        "photovoltaic system. This data is read out and output as JSON data records.",
    packages=["sma_data_provider"],
    install_requires=["modbus"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "sma_data_provider = sma_data_provider.cli:main"
        ]
    }
)
