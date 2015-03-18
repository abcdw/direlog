#!/usr/bin/env python
# encoding: utf-8
import sys
import re

from patterns import pre_patterns


def prepare(infilename, outfilename=None):
    """
    Apply pre_patterns from patterns to inputfile

    :infilename: input filename
    :outfilename: output filename for prepared text

    """

    if outfilename:
        outfile = open(outfilename, 'w')
    else:
        outfile = sys.stdout

    with open(infilename, 'r') as infile:
        for line in infile:
            result = line
            for pattern in pre_patterns:
                result = re.sub(pattern[0], pattern[1], result)
                outfile.write(result)

    if not outfile is sys.stdout:
        outfile.close()


def main():

    filename = 'error_log_test'
    filename = 'error_log'
    prepare(filename)

    pass

if __name__ == '__main__':
    main()
