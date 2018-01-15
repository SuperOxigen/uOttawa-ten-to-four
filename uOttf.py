#!/usr/bin/python
"""uOttawa Ten to Four.

Converts uOttawa 10 GPA System to 4 Point System.

Copyright (c) 2017 Alex Dale
See LICENSE for information.
"""

import argparse
import csv
import os
import sys


def ten_to_four(ten):
    """Ten to Four.

    A simple mapping from the 10 point system to
    the four point system.
    """
    return {
        10: 4.0,
        9: 3.9,
        8: 3.7,
        7: 3.3,
        6: 3.0,
        5: 2.3,
        4: 2.0,
        3: 1.3,
        2: 1.0,
        1: 0.0,
        0: 0.0
    }.get(ten)


def parse_arguments(args):
    """Parses Commandline Arguments."""
    parser = argparse.ArgumentParser(
        epilog=("Copyright (c) 2017 Alex Dale"
                " - See LICENCE"))

    parser.add_argument(
        "-i", "--input",
        help="Input CSV file.",
        type=str,
        required=True)

    parser.add_argument(
        "-o", "--output",
        help="Output CSV file.  Prints to console if not specified.",
        type=str,
        default=None)

    parser.add_argument(
        "-a", "--average",
        help="Prints average to console.",
        action="store_true")

    return parser.parse_args(args=args)


def main(args):
    """Main Program."""
    options = parse_arguments(args)

    inputfile = options.input

    if not os.path.isfile(inputfile):
        print("File does not exist! {}".format(inputfile))
        return

    with open(inputfile) as inputcsv:
        reader = csv.reader(inputcsv)

        if options.output is not None:
            outputcsv = open(options.output, mode="w")
        else:
            outputcsv = sys.stdout

        total = 0
        count = 0
        for row in reader:
            nrow = row[:]
            if len(row) >= 2 and row[1].isnumeric():
                four = ten_to_four(int(row[1]))
                total += four
                count += 1
                nrow[1] = four

            outputcsv.write("{}\n".format(",".join(
                [str(value) for value in nrow])))

        if options.output is not None:
            outputcsv.close()

    if options.average:
        print("Average: {:3.1f}".format(round(total / count, 1)))


if __name__ == "__main__":
    main(sys.argv[1:])
