
# AKT real time bus departure display for the [Display-o-Tron 3000](https://github.com/pimoroni/dot3k)

**Developed by:** Morten Amundsen

This program is written in Python. If you have a DOT3K, you can use this to see a real time list of bus departures from a bus stop of your choice.

- To get started, you'll need to install the required dependencies on your RPi. Head over to [Pimoroni's GitHub](https://github.com/pimoroni/dot3k) to get started.
- After installing the required dependencies, clone this repository to your RPi, and you're set!

## Run this in a terminal, and you should be good to go

```sh
curl -sS get.pimoroni.com/displayotron | bash
```

*If you're having issues, try:*
```sh
sudo pip install dot3k
```

## If you want the menu to start automatically on boot, type the following in a terminal:

```sh
sudo crontab -e
@reboot sh /home/AKT-bus-list/launcher.sh >/home/pi/logs/cronlog 2>&1
```
