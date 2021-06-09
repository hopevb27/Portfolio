Usbid: complete description and guide
========================================

Introduction
---------------

**Usbid** is a Python-based auxiliary cybersec tool for detection and logging of USB devices connected to a local machine. It is designed for creation of black and white lists of USB devices, as well as for checking if connected devices are allowed to connect in accordance with a pre-defined white list.

Feature List
--------------

Usbid has following features:

1. Detection of USB devices connected to the machine;
2. Logging of USB devices connected to the machine;
3. Comparison of credentials of connected USB devices with entries of an existing log (pre-defined black or white list).

Technical Description
------------------------

**System Requirements**

Minimum hardware requirements:

* x86 64-bit CPU (Intel / AMD architecture);
* 4 GB RAM;
* 5 GB free disk space.

Software and environment requirements:

* OS Linux / Windows / MacOS;
* Python 3;
* Python USB utilities library (see the **Troubleshooting** section).

**Components of the Program**

All components of the Usbid are incorporated into corresponding Python functions available through the easy-to-use terminal interface:

* _Detection component_ - a function responsible for detection of all USB devices connected to a local machine and demonstration of them in a terminal window. Each demonstrated device entry consists of a **vendor ID** and a **device ID** serialized in hexadecimals. The function can be applied for preprocessing or preliminary detection of USB devices connected to a local machine.
* _Log management component_ - a function responsible for creation of new Usbid logs. While creating a new log, the function also includes all detected USB devices into the log to be created. Each log entry consists of a **vendor ID** and a **device ID** serialized in hexadecimals. The function can be applied for creation of a device black or white list from scratch.
* _Logging component_ - a function responsible for adding of all detected USB devices into an existing _usblog.txt_ file. The function appends the connected USB devices to the existing device list. Each demonstrated device entry consists of a **vendor ID** and a **device ID** serialized in hexadecimals. The function can be applied for whitelistng or blacklisting of devices connected to a local machine.
* _Checking component_ - a function responsible for comparison of an existing _usblog.txt_ device log with USB devices detected on a local machine. The comparison is performed by creation of diffs between preprocessed maps containing **vendor** and **device IDs** serialized in hexadecimals. In case any device is not found in the existing device log, its credentials will be shown in the terminal.

**User Interface**

The Usbid user interface is designed in the CLI format and available in the system terminal after launching of the program.

It includes following commands:

* _new_ - create a new log with a user-defined name and include all detected USB devices into it.
* _accept_ - append all detected USB devices to the existing _usblog.txt_ log. If the _usblog.txt_ file does not exist in the program directory, it is created from scratch.
* _show_ - return all detected USB devices into the terminal output (STDOUT).
* _check_ - compare all detected USB devices with the list included into an existing _usblog.txt_ file. The comparison result is returned into the terminal output (STDOUT). If the _usblog.txt_ file does not exist in the program directory, it is created from scratch: in this case, all detected USB devices will be shown in the terminal output as missing in the list.
* _quit_ - exit the program.

**Logging Format Reference**

The Usbid logs are built in the colon-separated format. Each entry is written from a new line and includes following device credentials:

```
Vendor ID : Device ID\n
```

The device credentials are serialized in hexadecimals:

```
*** Vendor ID : Device ID ***
0x1210 : 0x25f4
```

The IDs of a vendor and a device are unique for each USB device type and a particular article.

While performing the `check` command, all existing entries of the log file are converted into a map complex data type, as well as the credentials of USB devices connected to a local machine and detected by the Usbid. Both maps are compared, and the entry pairs missing in the log map are displayed in the terminal output as not included into the log. In the same time, the entries present in both maps are displayed as existing in the log:

```
No entry in the log: Vendor ID: 0x1211 Device ID: 0x25f1
Vendor ID: 0x1210 Device ID: 0x25f4 - OK
```

User Guide
------------

**Launching the Program**

1. Place the _usbid.py_ file into a desired directory;
2. Enter following command in the terminal:

```
python3 usbid.py
``` 

3. When the program is launched, you will see the internal prompt:

```
>>>
``` 

**Creating New Log**

1. Launch the program;
2. Enter the `new` command in the internal command line of the program;
3. Enter a desired log name after the message `Enter new log name:`.

The new log containing all USB devices connected to your machine will be created in the program directory:

```
0x1210 : 0x25f4
``` 

**Logging Connected Devices**

1. Create a _usblog.txt_ device list in the program directory;
2. Launch the program;
3. Enter the `accept` command in the internal command line of the program.

The USB devices connected to your local machine will be appended in the end of an existing log:

```
0x1110 : 0x22a0
``` 

**Detection of Connected Devices**

1. Launch the program;
2. Enter the `show` command in the internal command line of the program.

The USB devices connected to your local machine will be displayed in the terminal output:

```
Vendor ID: 0x1210 : Device ID: 0x25f4
``` 

**Checking Connected Devices**

1. Place the pre-created _usblog.txt_ device log in the program directory;
2. Launch the program;
3. Enter the `check` command in the internal command line of the program.

If a USB device connected to your machine is not included into the _usblog.txt_, it will be displayed in the terminal output in the following message:

```
No entry in the log: Vendor ID: 0x1211 Device ID: 0x25f1
```

If a USB device connected to your machine is included into the _usblog.txt_, it will also be displayed in the terminal output:

```
Vendor ID: 0x1210 Device ID: 0x25f4 - OK
```

Troubleshooting
-----------------

**Python error while starting the program:**

```
import usb.core
ImportError: No module named usb.core
```

In case you use the Usbid on Windows, download and install the [Python USB library](https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/).

For apt-based Linux distros, download the `python-usb` package:

```
sudo apt install python-usb
```

**All devices are displayed as missing in the list while comparing with the use of the `check` command**

Make sure you have placed a pre-created _usblog.txt_ device log into the program directory.

If not, the program will create an empty _usblog.txt_ file and compare the map of detected devices with an empty map, and display all devices as missing.