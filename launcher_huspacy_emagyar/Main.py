import sys

from Launcher import Launcher

class Main():

    def __init__(self, config):
        self.launcher = Launcher(config)

    def launch(self):
        self.launcher.launch()
