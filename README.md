# quadLegas

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-3572A5.svg)](https://www.python.org/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-CB0000.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

quadLegas is a CLI Python application for UFABC students who want to find out who their new classmates are!

## Functionalities

With quadLegas you can:
* Import the enrollment document (example [here](http://prograd.ufabc.edu.br/pdf/_matriculas_deferidas_pos_ajuste_2019_3.pdf));
* Generate a *csv* file with the names of all your classmates;
* Generate a *csv* file with the names of all students in a class.

## Usage

<p align="center">
  <img width="650" src="https://raw.githubusercontent.com/pi-etro/quadLegas/master/img/menu.gif">
</p>

## Installation

quadLegas uses Python 3 and the following Python libraries:
* [colorama](https://github.com/tartley/colorama)
* [cryptography](https://cryptography.io/en/latest/)
* os (Python Standard Library)
* [pandas](https://github.com/pandas-dev/pandas)
* sys (Python Standard Library)
* [tabula-py](https://github.com/chezou/tabula-py)

### Linux
#### Standalone
Currently there is a standalone executable that should work for linux users, you can download it [here](https://github.com/pi-etro/quadLegas/releases/latest/download/quadlegas). Give permission to read and execute with:
```bash
chmod +rx quadlegas
```
And run with:
```bash
./quadlegas
```

#### Source code
If you don't want the standalone version, install the libraries mentioned. You can install them with pip3:
```bash
pip3 install colorama
pip3 install cryptography
pip3 install pandas
pip3 install tabula-py
```
Download the source code [here](https://github.com/pi-etro/quadLegas/archive/master.zip) and extract it. In the extrated folder use:
```bash
chmod +rx quadlegas.py
```
And run with:
```bash
./quadlegas.py
```

### Others
I haven't tested quadLegas on other OS, but if you manage to install the Python libraries mentioned, you should be able to run it.

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)
