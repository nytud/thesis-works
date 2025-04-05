import sys

from Launcher import Launcher

class Main():

    def __init__(self):
        config = sys.argv[1:]
        config.append("-nongraphic")
        self.launcher = Launcher(config)
        print("Launcher indul")

    def launch(self):
        self.launcher.launch()
    

main = Main()
main.launch()