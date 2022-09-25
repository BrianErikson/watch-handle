from argparse import ArgumentParser
import subprocess
import os
from collections import OrderedDict
from time import sleep
import socket

def handle64_output(process_str: str):
    return subprocess.run(['handle64.exe', '-p', process_str], stdout=subprocess.PIPE, text=True).stdout.splitlines()


def main(process_str):
    all_output = set()

    while True:
        output = set(handle64_output(process_str))
        diff = '\n'.join(sorted(all_output.symmetric_difference(output)))
        if len(diff) > 0:
            os.system('clear')
            print(diff)

        all_output.union(output)
        sleep(0.1)


if __name__ == '__main__':
    parser = ArgumentParser(prog='watch-handle', usage='watch-handle -p <process>')
    parser.add_argument('-p', type=str, nargs=1, help='Process name or id')

    args = parser.parse_args()
    main(args.p[0])