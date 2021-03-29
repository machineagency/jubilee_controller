If you're looking for a standard operating procedure, check out the [quickstart](docs/quickstart.md).

## Intro
This project wraps a python interface around the existing Duet HTTP Interface for controlling Jubilee in python.

## Connecting to Jubilee
There are three ways to connect to Jubilee and execute code: (1) locally and (2) with a separate PC over a network connection.

They look like this:

### Local Connection (Duet 3 with SBC Only)
<img src="https://github.com/machineagency/jubilee_python_driver/blob/master/docs/pics/jubilee_duet3_local_connection.png">
In this mode, everything runs on the onboard Raspberry Pi, and keyboard and mouse are plugged directly into the Pi.

### Local Connection through SSH (Duet 3 with SBC Only)
TODO: image here.

In this mode, everything runs on the onboard Raspberry Pi, but connection is made to the Pi via a remote SSH session from another PC.
Internet access is also shared from the PC that's remoting into the Pi through network sharing.
[Linux Internet Sharing Setup](https://www.raspberrypi.org/forums/viewtopic.php?t=10916)

### Closed Network Connection (Duet 2 or 3)
<img src="https://github.com/machineagency/jubilee_python_driver/blob/master/docs/pics/jubilee_duet_closed_network_connection.png">
In this mode, the Python protocol runs on a separate pc with this software package installed.
It will run as long as it is connected to the PC connected to it.

When running the machine in this mode, note that turning off your PC or losing the network connection will halt the machine mid-execution.
Furthermore, a laggy network connection will cause the machine to lag.

## Installation
If you are running this code locally, clone this repository onto Jubilee's attached Raspberry Pi.
If you are running it over a network connection, clone it onto your PC.

Then, from within this directory (the one with this README in it), install the project via pip with ....
```
pip3 install -e .
```

Now you can spin up a connection to Jubilee by importing the driver.

## API
There are 2 ways of interacting with the machine:
(1) directly through a python script, and
(2) interactively through a command prompt.

## Python Script Mode
After installing this package with pip, you should be able to simply import it in python:

If you are running the code locally, the code will look like this:
```python
# TODO: schnazzy python example here.
```
If you are running the code over a network from a separate PC, the code may look like this:
```python
# TODO: schnazzy pyton example here using ip address or jubilee.local
```
Here the above *address* argument is the ip address of Jubilee as it appears on your network.

## Prompt Mode
You can interactively control Jubilee through a custom prompt.
To interact with the prompt, spin it up from the python shell with:

```python
from sonication_station.sonication_station import SonicationStation
with SonicationStation() as jubilee:
    jubilee.cmdloop()
```

or, from the command line:

```
sudo path/to/sonication_station/sonication_station.py
```

This will drop you into an interactive prompt that looks like this:
```
JUBILEE Controller
>>> 

```
This mode lets you input commands one at a time.

In this mode you can:

* home the machine
* execute movement commands
* pickup and park tools
* control the machine with the keyboard arrow keys

To see the list of supported commands, press TAB twice.
This mode also supports TAB completion, that is, if you start typing a command and press TAB twice, the prompt will either attempt to auto-complete any possibilities or show you a list of possible completions.
To get help on any command, simply type:

```
>>> help command_name_here
```