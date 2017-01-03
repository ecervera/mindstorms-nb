# Mindstorms Notebooks

Examples and exercises for LEGO&reg; Mindstorms NXT and EV3 mobile robots.

The code consists of [Jupyter notebooks](http://jupyter.org/) 
running in a laptop or desktop computer, 
which communicates with the robots via Bluetooth (NXT), or WiFi (EV3).

The NXT runs its standard firmware, but the EV3 should run the 
[ev3dev](http://www.ev3dev.org/) operating system.

## Prerequisites

* NXT
  * [PyBluez](https://github.com/karulis/pybluez)
  * [NXT-Python](https://github.com/Eelviny/nxt-python)
* EV3
  * [ev3dev](http://www.ev3dev.org/)
  * [RPyC](http://ev3dev-lang-python.readthedocs.io/en/latest/rpyc.html)
* Computer
  * Python 3.x
  * [Jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html)

## Setup

### NXT

Activate Bluetooth and pair your robot and computer.

### EV3

1. Connect the robot to the same WiFi that your computer.

2. [Install RPyC](http://ev3dev-lang-python.readthedocs.io/en/latest/rpyc.html)

### Computer

We recommend using Miniconda and creating an environment:

* [Conda quick install](http://conda.pydata.org/docs/install/quick.html)
  * `conda create --name py34 python=3.4.2`
  * `source activate py34`
  * `conda install jupyter matplotlib`
* If using a NXT:
  * `pip install pybluez`
  * Install [NXT-python](https://github.com/Eelviny/nxt-python)
* If using an EV3:
  * `pip install rpyc`

## Usage

### NXT

Switch it on, that's all!

### EV3

* Switch it on.
* Run the script `rpyc_classic.py` as explained [here](http://ev3dev-lang-python.readthedocs.io/en/latest/rpyc.html).

### Computer

Download, run `jupyter notebook index.ipynb` in the root folder, and enjoy!

### Try-a-Bot: an open source guide for robot programming

Developed by:
[![Robotic Intelligence Lab @ UJI](img/logo/robinlab.png "Robotic Intelligence Lab @ UJI")](http://robinlab.uji.es)

Sponsored by:
<table>
<tr>
<td style="border:1px solid #ffffff ;"><a href="http://www.ieee-ras.org"><img src="img/logo/ras.png"></a></td>
<td style="border:1px solid #ffffff ;"><a href="http://www.cyberbotics.com"><img src="img/logo/cyberbotics.png"></a></td>
<td style="border:1px solid #ffffff ;"><a href="http://www.theconstructsim.com"><img src="img/logo/theconstruct.png"></a></td>
</tr>
</table>

Follow us:
<table>
<tr>
<td style="border:1px solid #ffffff ;"><a href="https://www.facebook.com/RobotProgrammingNetwork"><img src="img/logo/facebook.png"></a></td>
<td style="border:1px solid #ffffff ;"><a href="https://www.youtube.com/user/robotprogrammingnet"><img src="img/logo/youtube.png"></a></td>
</tr>
</table>
