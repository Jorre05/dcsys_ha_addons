# Home Assistant DCSys Add-on

__Alle vroegere dcsysxyz processen in een HA add-on__
__dcsysfluviusd hoeft niet meer__

![Supports aarch64 Architecture][aarch64-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg

```c
DCSys dcsysbalanced usage:
----------------------
dcsysbalanced [-s sleeptime] [-v debuglevel]
  -s sleeptime      : post switch sleeptime
  -v debuglevel     : debuglevel

DCSys dcsysfluviusd usage:
----------------------
dcsysfluviusd -h hostname [-p port] [-v debuglevel]
  -h hostname        : fluvius hostname
  -p port            : port
  -v debuglevel      : debuglevel

DCSys dcsysmodbusd usage:
----------------------
getmodbusvalues -h hostname [-v debuglevel] [-c config_filename] [-c outputpath] [-s sleeptime]
  -h hostname        : Inverter hostname
  -v debuglevel      : debuglevel
  -s sleeptime       : sleeptime
  -c config_filename : Config filename
  -o outputpath      : result ouput file path
```
