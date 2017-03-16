#!/usr/bin/env python
print("""
Initiated
""")

import sys
import subprocess
import socket

sys.path.append("../../")

import dot3k.joystick as joystick
import dot3k.lcd as lcd
import dot3k.backlight as backlight
from plugins.graph import IPAddress, GraphTemp, GraphCPU
from plugins.clock import Clock
from plugins.cust import Time
from plugins.bus import Kvadraturen, UiA
from plugins.launcher import SysShutdown, SysReboot, LaunchMenu
import time

backlight.rgb(255, 255, 255)

menu = Menu(
    None,
    lcd,
    5)

"""
If you want menu items to appear in a defined order, you must
add them one at a time using 'add_item'. This method accepts
a plugin instance, plus the path where you want it to appear.

Instances of classes derived from MenuOption can
be used as menu items to show information or change settings.

See GraphTemp, GraphCPU, Contrast and Backlight for examples.
"""

menu.add_item('Clock', Clock())
menu.add_item('Status/IP', IPAddress())
menu.add_item('Status/CPU', GraphCPU())
menu.add_item('Status/Temp', GraphTemp())
menu.add_item('Info', Time())
menu.add_item('Scripts/ShutDown', SysShutdown())
menu.add_item('Scripts/Reboot', SysReboot())
menu.add_item('Scripts/Launcher', LaunchMenu())
menu.add_item('Buss/Kvadraturen', Kvadraturen())    # Replace "Buss/Kvadraturen" with "Buss/A_Name_Of_Your_Choice" and "Kvadraturen()" with the "Method_Name()" defined in bus.py
menu.add_item('Buss/UiA', UiA())                    # Replace "Buss/UiA" with "Buss/A_Name_Of_Your_Choice" and "UiA()" with the "Method_Name()" defined in bus.py

"""
You can use anything to control dot3k.menu,
but you'll probably want to use dot3k.joystick
"""
REPEAT_DELAY = 0.5


@joystick.on(joystick.UP)
def handle_up(pin):
    menu.up()
    joystick.repeat(joystick.UP, menu.up, REPEAT_DELAY, 0.9)


@joystick.on(joystick.DOWN)
def handle_down(pin):
    menu.down()
    joystick.repeat(joystick.DOWN, menu.down, REPEAT_DELAY, 0.9)


@joystick.on(joystick.LEFT)
def handle_left(pin):
    menu.left()
    joystick.repeat(joystick.LEFT, menu.left, REPEAT_DELAY, 0.9)


@joystick.on(joystick.RIGHT)
def handle_right(pin):
    menu.right()
    joystick.repeat(joystick.RIGHT, menu.right, REPEAT_DELAY, 0.9)


@joystick.on(joystick.BUTTON)
def handle_button(pin):
    menu.select()


while 1:
    menu.redraw()
    time.sleep(0.05)