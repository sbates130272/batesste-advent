#!/usr/bin/env python3
#
# batesste-advent.py
#
# A simple script to generate a fair allocation of doors across one or
# more advent calandars.

import argparse
import random

def list_of_names(arg):
    return arg.split(',')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Generate a fair allocation of advent calandar doors.',
        epilog='I hope you have been very good this year! Love Santa')
    parser.add_argument('-d', '--days', type=int, default=24,
                        help="Number of days in advent.")
    parser.add_argument('-n', '--number', type=int, default=1,
                        help="Number of advent calandars")
    parser.add_argument('--names', type=list_of_names,
                        help="A list of the names of our peeps.")
    args = parser.parse_args()

    people = len(args.names)
    repeats = int(args.days/people)

    for x in range(args.number):
        advent = []
        for y in range(repeats):
            random.shuffle(args.names)
            advent+=args.names

        print(advent)
