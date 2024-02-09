# SMA Device Data Collector

With the SMA device data collector, it is possible to read out data via the web server contained in the device, which also appears on the WebGUI. This data can then be further processed in other applications.

The SMA device data collector is currently under development and can currently read out the following data:

* Session Id assigned by the device.

## Compatibility list

Data can currently be obtained from the following SMA devices:

* SMA SUNNY TRIPOWER 10.0 SE

If further devices are operated with this software, this list will be extended. The relevant information is requested here.

## Requirements

The following requirements must be met in order to operate this software:

* an SMA device integrated in the local network which is compatible, see compatibility list
* A computer connected to the local network on which [Python](https://www.python.org/) is installed (Python 3.10 or higher)

## Installation

1. download this GitHub repository as [ZIP archive](https://github.com/hjboehle/SMA-Data-Provider/archive/refs/heads/main.zip)
2. unpack the ZIP archive into a directory of your choice
3. change to the directory with the unpacked repository
4. create the environment variable `PYTHONPATH=directory_of_your_choice/src/sma_data_provider`
5. create the environment variable `SMA_DEVICE_RIGHT=usr`
6. create the environment variable `SMA_DEVICE_PASSWORD=<password of the user>`
7. call the Python script with `python src/sma_data_provider/main.py --ip_address <IP address of your SMA device>`

Users who work with `git` can of course also clone the repository to a directory of their choice.
