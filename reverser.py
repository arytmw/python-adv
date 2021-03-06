import argparse #sudo pip3.6 install argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in reverse.')
parser.add_argument('filename',help='The name of the file to read in reverse.')
parser.add_argument('--limit','-l',type=int,help='The number of lines to read.')
parser.add_argument('--version','-v',action='version',version='1.0 by Ayush')

args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError:
    print("Error: File not found. Please check path.")
    sys.exit(1)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if limit:
            lines = lines[0:limit]

        for line in lines:
            print(line.strip())
