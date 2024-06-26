# 1. Define a class called TV.
class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if self.is_on and 1 <= channel <= 120:
            self.channel = channel

    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume_level):
        if self.is_on and 1 <= volume_level <= 7:
            self.volume_level = volume_level

    def channel_up(self):
        if self.is_on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.is_on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.is_on and self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        if self.is_on and self.volume_level > 1:
            self.volume_level -= 1

''' Create another file and named that into test_tv.py,
this will be the test driver that will create two objects
from the Class TV and will produced the output '''