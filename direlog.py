#!/usr/bin/env python
# encoding: utf-8
import sys
import re
import argparse
import fileinput

from argparse import RawDescriptionHelpFormatter

from patterns import pre_patterns


def prepare(infile, outfile=sys.stdout):
    """
    Apply pre_patterns from patterns to infile

    :infile: input file

    """

    try:
        for line in infile:
            result = line
            for pattern in pre_patterns:
                result = re.sub(pattern[0], pattern[1], result, re.VERBOSE)
            outfile.write(result)
    except (KeyboardInterrupt):
        pass
    except:
        raise


def main():
    parser = argparse.ArgumentParser(description=\
    """
    Parse file[s]\n\n
    examlpe: cat error_log | tail -n 1000 | ./direlog.py
    """, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('file', nargs='*', default=[],
                        help='file[s] to do some work')
    parser.add_argument('-s', '--stat', action='store_const', const=True,
                        help='get statistics')
    args = parser.parse_args()

    input_stream = fileinput.input(args.stat)


    prepare(input_stream)

    pass

if __name__ == '__main__':
    main()
