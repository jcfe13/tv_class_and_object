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
