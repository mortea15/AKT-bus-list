import psutil
import subprocess
import time
import socket
import fcntl
import struct
import sys
from dot3k.menu import MenuOption


def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate()[0]
    return output


class SysShutdown(MenuOption):
    """Shuts down the Raspberry Pi"""

    def __init__(self):
        self.last = self.millis()
        MenuOption.__init__(self)

    def redraw(self, menu):
        shutdown = "sudo shutdown -h now"

        now = self.millis()
        if now - self.last < 1000 * 5:
            return False

        a = run_cmd(shutdown)

        menu.write_row(0, 'RPi Shutdown')
        menu.write_row(1, '')
        menu.write_row(2, time.strftime('  %a %H:%M:%S  '))


class SysReboot(MenuOption):
    """Reboots the Raspberry Pi"""

    def __init__(self):
        self.last = self.millis()
        MenuOption.__init__(self)

    def redraw(self, menu):
        reboot = "sudo reboot"

        now = self.millis()
        if now - self.last < 1000 * 5:
            return False

        a = run_cmd(reboot)

        menu.write_row(0, 'RPI Reboot')
        menu.write_row(1, '')
        menu.write_row(2, time.strftime('  %a %H:%M:%S  '))

class LaunchMenu(MenuOption):

    def __init__(self):
        self.last = self.millis()
        MenuOption.__init__(self)

    """def right(self):
        os.system("menu.py")
        return True"""

    def redraw(self, menu):
        location = "cd AKT-bus-list/menu"
        file = "sudo ./menu.py"

        now = self.millis()
        if now - self.last < 1000 * 5:
            return False

        a = run_cmd(location)
        b = run_cmd(file)

        menu.write_row(0, 'Launch menu')
        menu.write_row(1, '')
        menu.write_row(2, time.strftime('  %a %H:%M:%S  '))