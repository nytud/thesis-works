import sys

from Launcher import Launcher


def main():
    launcher = Launcher(sys.argv[1:])
    print("Launcher indul")

    launcher.launch()
    

if __name__ == "__main__":
    main()
 