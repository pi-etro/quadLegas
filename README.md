<p align="center">
    <img src="https://raw.githubusercontent.com/pi-etro/quadLegas/master/img/quadLegas.png" width="598">
</p>
<p align="center">
    <a href="https://www.python.org/" alt="Made with Python">
        <img src="https://img.shields.io/badge/Made%20with-Python-3572A5.svg" /></a>
    <a href="https://www.gnu.org/licenses/gpl-3.0.html" alt="GPLv3">
        <img src="https://img.shields.io/badge/License-GPLv3-CB0000.svg" /></a>
</p>
<p align="center">
quadLegas is a CLI Python application to find out your new UFABC classmates!
</p>

## Features

<p align="center">
  <img width="660" src="https://raw.githubusercontent.com/pi-etro/quadLegas/master/img/new_menu.gif">
</p>

With quadLegas you can:
* Generate a *csv* file with the names of all your classmates;
* Generate a *csv* file with the names of all students in a class;

## Table of Contents

* [Installation](#Installation)
  * [Linux](#Linux)
  * [Others](#Others)
* [Usage](#Usage)
* [About](#About)
* [License](#License)

## Installation

quadLegas uses Python 3 and the following Python libraries:
* [colorama](https://github.com/tartley/colorama)
* [cryptography](https://cryptography.io/en/latest/)
* os (Python Standard Library)
* [pandas](https://github.com/pandas-dev/pandas)
* sys (Python Standard Library)

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
If you don't want the standalone version, install the libraries [mentioned](#Installation). You can install them with pip3:
```bash
pip3 install colorama cryptography pandas
```
Download the source code [here](https://github.com/pi-etro/quadLegas/archive/v1.1.zip) and extract it. In the extrated folder use:
```bash
chmod +rx quadlegas.py
```
And run with:
```bash
./quadlegas.py
```

### Others
I haven't tested quadLegas on other OS, but if you manage to install the Python libraries [mentioned](#Installation) you should be able to run it.

## Usage

After you started quadLegas, select option `1` to list all students who are in the same classes as you - enter your university ID (RA) and the path to the *csv* file (`/path/to/file.csv`) - or option `2` to list all students from one or more classes - enter the number of classes to consult, the code for each class and the path to the *csv* file.

In the output *csv* file, each column each column corresponds to a class with the class code as header, each row has the students' name or the university ID (RA) - in case quadLegas doesn't know the name associated with the ID.

Enter `0` any time to return to the menu and `4` to exit the menu and quit quadLegas.

## About

This project was done as a Python programming practice and for no other purpose, so it is not optimized and may present errors. You are welcome to contribute!

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)
