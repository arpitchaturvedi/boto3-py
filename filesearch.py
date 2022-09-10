# find like utility where supply the directory and file to search
# eg : find /etc/ -iname hosts
# User friendly
#python3 search.py -h
#python3 search.py <dir name> <file name> --> on the command line
import os
import argparse

my_parser = argparse.ArgumentParser(description= 'Reading the dir path')
my_parser.add_argument("pathname", help="please enter the dir path")
#my_parser.add_argument("filesearch", help="please enter the filename")
args = my_parser.parse_args()

for dirname, dirpath, filename in os.walk(args.pathname):
    for file in filename:
        if file.endswith('.conf'):
            print(os.path.join(dirname, file))
