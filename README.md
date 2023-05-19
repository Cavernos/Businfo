# Businfo - Windows, Linux

[![Latest Release](https://img.shields.io/github/v/release/ViaVersion/ViaVersion)](https://viaversion.com)
[![Build Status](https://github.com/ViaVersion/ViaVersion/actions/workflows/gradle.yml/badge.svg?branch=master)](https://github.com/ViaVersion/ViaVersion/actions)
[![Discord](https://img.shields.io/badge/chat-on%20discord-blue.svg)](https://viaversion.com/discord)

**Businfo system in python**




**Build Configuration on Windows:**
```shell
git clone https://github.com/Cavernos/Businfo.git \
cd Businfo \
python -m pip install -r requirements.txt \
pyinstaller businfo_windows.spec \
.\dist\Businfo_windows\Businfo.exe
```

**Build Configuration on Linux:**
```shell
git clone https://github.com/Cavernos/Businfo.git \
cd Businfo \
python -m pip install -r requirements.txt
pyinstaller businfo_linux.spec
./dist/Businfo_linux/Businfo.sh
```

**Exemple of JSON FILE**
```JSON
{
  "number": 2,
  "line": 20,
  "ziel": 200,
  "start": "Congress \t  \t Ibk",
  "dest": "Hungerburg \t \t Ibk",
  "next_start": "19:15:00",
  "next_stop": 0,
  "max_stop": 9,
  "stops": {
    "0": {
      "name": "Congress \t  \t Ibk",
      "horaire": "19:15:00"
    },
    "1": {
      "name": "Hungerburg \t \t Ibk",
      "horaire": "19:25:00"
    },
    "2": {
      "name": "2",
      "horaire": "19:35:00"
    },
    "3": {
      "name": "3",
      "horaire": "19:45:00"
    },
    "4": {
      "name": "4",
      "horaire": "20:25:00"
    },
    "5": {
      "name": "5",
      "horaire": "21:25:00"
    },
    "6": {
      "name": "6",
      "horaire": "15:25:00"
    },
    "7": {
      "name": "7",
      "horaire": "19:25:00"
    },
    "8": {
      "name": "8",
      "horaire": "19:25:00"
    },
    "9": {
      "name": "9",
      "horaire": "19:25:00"
    }
  }
}

{"GPRS":1,"dest":"Bauernhof","game_time":"21:14:44","line":76,"max_stop":7,"next_start":"21:37:00","next_stop":3,"start":"Krankenhaus","stops":{"0":{"name":"Krankenhaus"},"1":{"name":"Krankenhaus"},"2":{"name":"Krankenhaus"},"3":{"name":"Krankenhaus"},"4":{"name":"Krankenhaus"},"5":{"name":"Krankenhaus"},"6":{"name":"Krankenhaus"},"7":{"name":"Krankenhaus"}},"tt_delay":"-24:34","ziel":107}
```

License
--------
The entirety of the [API directory](api) (including the legacy API directory) is licensed under the MIT License; see [licenses/MIT.md](licenses/MIT.md) for
details.

Everything else, unless explicitly stated otherwise, is licensed under the GNU General Public License, including the end
product as a whole; see [licenses/GPL.md](licenses/GPL.md) for details.

Special thanks to all our [Contributors](https://github.com/ViaVersion/ViaVersion/graphs/contributors).