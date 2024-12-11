#!/usr/bin/env python3

'''
File to load command line arguments
'''

from argparse import ArgumentParser


def parse():
    ''' Parse command line arguments '''
    desc = "Maze solver python script"
    ap = ArgumentParser(description=desc)
    ap.add_argument('-f', '--file',
                    type=str,
                    required=True,
                    help="Path to file")
    ap.add_argument('-t', '--mtype',
                    type=int,
                    required=True,
                    default=1,
                    help="Type of maze that is loaded, can be either 1 or 2")
    ap.add_argument('-d', '--delay',
                    type=int,
                    required=False,
                    default=1000,
                    help="Delay between draw update in ms")
    return ap.parse_args()


if __name__ == "__main__":
    args = parse()
    print(f"File path: {args.file}, delay: {args.delay}")
