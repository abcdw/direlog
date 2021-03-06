#!/usr/bin/env python
# encoding: utf-8
import sys
import re
import argparse
import fileinput

from argparse import RawDescriptionHelpFormatter

from patterns import pre_patterns


def prepare(input_stream, outfile=sys.stdout):
    """
    Apply pre_patterns from patterns to input_stream

    :input_stream: input stream

    """
    compiled_patterns = []
    for pattern in pre_patterns:
        compiled_patterns.append((re.compile(pattern[0]), pattern[1]))

    try:
        for line in input_stream:
            result = line
            for pattern in compiled_patterns:
                result = pattern[0].sub(pattern[1], result, re.VERBOSE)
            outfile.write(result)
    except (KeyboardInterrupt):
        pass
    except:
        raise


def main():
    parser = argparse.ArgumentParser(description=\
    """
        Prepare file[s]\n\n
        example: cat error_log | tail -n 1000 | ./%(prog)s
    """, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('file', nargs='*', default=[],
                        help='file[s] to do some work')
    args = parser.parse_args()

    input_stream = fileinput.input(args.file)


    prepare(input_stream)

    pass

if __name__ == '__main__':
    main()
