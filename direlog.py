#!/usr/bin/env python
# encoding: utf-8
import sys
import re
import argparse

from patterns import pre_patterns


def prepare(infile):
    """
    Apply pre_patterns from patterns to infile

    :infile: input file

    """

    try:
        for line in infile:
            result = line
            for pattern in pre_patterns:
                result = re.sub(pattern[0], pattern[1], result)
                sys.stdout.write(result)
    except (KeyboardInterrupt):
        pass


def main():
    parser = argparse.ArgumentParser(description='Parse file[s]')
    parser.add_argument('file', nargs='*', default=[],
                        help='file[s] to do some work')
    parser.add_argument('-s', '--stat', action='store_const', const=True,
                        help='get statistics')
    args = parser.parse_args()

    if not args.file:
        prepare(sys.stdin)
    else:
        for filename in args.file:
            with open(filename, 'r') as f:
                prepare(f)

    # if outfilename:
        # outfile = open(outfilename, 'w')
    # else:
        # outfile = sys.stdout

    pass

if __name__ == '__main__':
    main()
