## py-linux-ports
Check Linux System Port's Status

[![Build Status](https://app.travis-ci.com/sujitmandal/py-linux-ports.svg?branch=master)](https://app.travis-ci.com/sujitmandal/py-linux-ports) ![GitHub license](https://img.shields.io/github/license/sujitmandal/py-linux-ports) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-linux-ports) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/py-linux-ports)  ![PyPI](https://img.shields.io/pypi/v/py-linux-ports) [![Conda Version](https://img.shields.io/conda/vn/conda-forge/py-linux-ports.svg)](https://anaconda.org/conda-forge/py-linux-ports) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/py-linux-ports/badges/version.svg)](https://anaconda.org/conda-forge/py-linux-ports) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/py-linux-ports/badges/installer/conda.svg)](https://conda.anaconda.org/conda-forge) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/py-linux-ports/badges/platforms.svg)](https://anaconda.org/conda-forge/py-linux-ports) [![Conda Recipe](https://img.shields.io/badge/recipe-py--linux--ports-green.svg)](https://anaconda.org/conda-forge/py-linux-ports) ![](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/py-linux-ports-feedstock?branchName=main)


[![Downloads](https://pepy.tech/badge/py-linux-ports)](https://pepy.tech/project/py-linux-ports)


## Package Installation  : 
```
pip install py-linux-ports
```
[Package Link](https://pypi.org/project/py-linux-ports/)

```
conda install py-linux-ports
```
[Conda Package Link](https://anaconda.org/conda-forge/py-linux-ports)


[py-linux-ports-feedstoc](https://github.com/conda-forge/py-linux-ports-feedstock)

## Py-Linux-Port's: 
```python
import json
from PyLinuxPorts.PyLinuxPorts import portScan 

IpAddress = "192.168.43.133"
PortNumber = 65000

result  = portScan(IpAddress, PortNumber)

print(json.dumps(result, indent=4))

with open('result.json', 'w') as i:
    json.dump(result, i)
```

## License:
MIT Licensed

## Author:
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)
