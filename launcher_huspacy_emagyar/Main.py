import sys

from Launcher import Launcher

class Main():

    def __init__(self):
        self.launcher = Launcher(sys.argv[1:])
        #print("Launcher indul")

    def launch(self):
        self.launcher.launch()
    

#main = Main()
#main.launch()