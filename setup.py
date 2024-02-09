"""module setup"""

from setuptools import setup

setup(
    name="SMA Device Data Collector",
    version="0.1.0",
    author="Hans Jürgen Böhle",
    author_email="hj@boehle.info",
    url="https://github.com/hjboehle",
    license='MIT',
    description="Data Provider for SMA Sunny Home Manager 2.0",
    long_description="SMA devices shows data in a WebGUI from the connected " \
        "photovoltaic system. This data is read out and output as JSON data records.",
    packages=["sma_data_collector"],
    install_requires=["modbus"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "sma_data_collector = sma_data_collector.cli:main"
        ]
    }
)
