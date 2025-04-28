
from pydiconde import Diconde
import sys
import json

def main():
    if len(sys.argv) < 2:
        print("missing file path")
        return

    data = json.load(open(sys.argv[1]))
    diconde_file = Diconde()
