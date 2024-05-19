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
    