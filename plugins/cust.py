# -*- coding: utf-8 -*-
from dot3k.menu import MenuOption
import time
import socket
import fcntl
import struct


class IP(MenuOption):
    """
    A plugin which gets the IP address for wlan0
    and displays them on the screen.
    """

    def __init__(self):
        self.mode = 0
        self.wlan0 = self.get_addr('wlan0')
        self.is_setup = False
        MenuOption.__init__(self)

    def get_addr(self, ifname):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15].encode('utf-8'))
            )[20:24])
        except IOError:
            return 'Not Found!'

    def redraw(self, menu):
        if not self.is_setup:
            self.is_setup = True

        menu.write_row(0, self.wlan0)


class Time(MenuOption):
    def __init__(self):
        # IP
        self.wlan0 = self.get_addr('wlan0')
        self.mode = 0

        # TIMEDATE
        self.running = False

        # if backlight is None:
        # import dot3k.backlight
        # self.backlight = dot3k.backlight
        # else:
        # self.backlight = backlight

        self.option_time = 0

        # self.dim_hour = 23
        # self.bright_hour = 10

        self.is_setup = False

        MenuOption.__init__(self)

    # IP
    def get_addr(self, ifname):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15].encode('utf-8'))
            )[20:24])
        except IOError:
            return 'Not Found!'

    def begin(self):
        self.is_setup = False
        self.running = True

    def setup(self, config):
        MenuOption.setup(self, config)
        self.load_options()

        # def set_backlight(self, brightness):
        # brightness += 0.01
        # if brightness > 1.0:
        # brightness = 1.0
        # r = int(int(self.get_option('Backlight', 'r')) * brightness)
        # g = int(int(self.get_option('Backlight', 'g')) * brightness)
        # b = int(int(self.get_option('Backlight', 'b')) * brightness)
        # if self.backlight is not None:
        # self.backlight.rgb(r, g, b)

    def update_options(self):
        # self.set_option('Clock', 'dim', str(self.dim_hour))
        # self.set_option('Clock', 'bright', str(self.bright_hour))
        '''getrekt'''

    def load_options(self):
        # self.dim_hour = int(self.get_option('Clock', 'dim', str(self.dim_hour)))
        # self.bright_hour = int(self.get_option('Clock', 'bright', str(self.bright_hour)))
        '''get rekt'''

    def cleanup(self):
        self.running = False
        time.sleep(0.01)
        # self.set_backlight(1.0)
        self.is_setup = False

    def left(self):
        return False
        self.update_options()
        self.option_time = self.millis()
        return True

    def right(self):
        self.update_options()
        self.option_time = self.millis()
        return True

    def up(self):
        self.mode = (self.mode - 1) % len(self.modes)
        self.option_time = self.millis()
        return True

    def down(self):
        self.mode = (self.mode + 1) % len(self.modes)
        self.option_time = self.millis()
        return True

    def redraw(self, menu):
        if not self.running:
            return False

        if self.millis() - self.option_time > 5000 and self.option_time > 0:
            self.option_time = 0
            self.mode = 0

        if not self.is_setup:
            menu.lcd.create_char(4, [0, 4, 14, 0, 0, 14, 4, 0])  # Up down arrow
            menu.lcd.create_char(5, [0, 0, 10, 27, 10, 0, 0, 0])  # Left right arrow
            self.is_setup = True

        year = int(time.strftime('%Y'))
        hour = float(time.strftime('%H'))
        brightness = 1.0
        # if hour > self.dim_hour:
        # brightness = 1.0 - ((hour - self.dim_hour) / (24.0 - self.dim_hour))
        # elif hour < self.bright_hour:
        # brightness = 1.0 * (hour / self.bright_hour)

        # self.set_backlight(brightness)

        menu.write_row(0, self.wlan0)
        menu.write_row(1, time.strftime('%H:%M:%S'))

        if self.idling:
            menu.clear_row(2)
            return True

        aday = time.strftime('%a')
        day = aday[:2]
        ayear = time.strftime('%Y')
        year = ayear[2:]
        bottom_row = time.strftime(day + ' %d/%m/' + year + ', U%W')

        menu.write_row(2, bottom_row)