

import sys
import argparse
import os.path
from os import path

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-p', action="store", dest="platform", default="git")
parser.add_argument('-f', action="store", dest="fileName", required=True)

args = parser.parse_args()

if not path.exists(args.fileName):
	print("file " + str(args.fileName) + "doesn't exist")
	sys.exit(1)

with open(args.fileName) as f:
    with open("fixedFile.csv", "w") as f1:
        for line in f:
          	f1.write(line)  
