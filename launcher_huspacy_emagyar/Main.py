import sys

from Launcher import Launcher


def main():
    launcher = Launcher(sys.argv[1:])
    print("Launcher indul")

    launcher.launch()
    
    launcher.compare_tokens()
    launcher.compare_morph()
    launcher.compare_lemma()
    launcher.compare_pos()
    launcher.compare_dep()
    launcher.compare_ner()

if __name__ == "__main__":
    main()
 