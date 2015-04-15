#!/usr/bin/env python
# encoding: utf-8

import sys
import re
import argparse
import fileinput
import copy

from argparse import RawDescriptionHelpFormatter

from patterns import main_patterns

def show_snippets(input_stream, patterns=main_patterns):
    """show snippets for patterns

    :input_stream: input stream
    :patterns: patterns that need to look
    :returns: None

    """

    LINES_ABOVE = 3
    LINES_BELOW = 3

    class Snippet(object):
        def __init__(self, lines_above, line):
            self.text = copy.copy(lines_above)
            self.matched_line = line

        def full(self):
            return len(self.text) >= LINES_ABOVE + LINES_BELOW + 1

        def add(self, line):
            self.text.append(line)

        def show(self):
            print self.text
            print '\n'


    class SnippetsQueue(object):
        def __init__(self):
            self.snippets = []

        def push(self, snippet):
            self.snippets.append(snippet)

        def add(self, line):
            for snippet in self.snippets:
                if snippet.full():
                    snippet.show()
                    self.snippets.remove(snippet) # TODO: improve speed
                else:
                    snippet.add(line)


    snippets_queue = SnippetsQueue()

    lines_above = [''] * LINES_ABOVE

    # print lines_above
    for line in input_stream:
        lines_above.append(line)
        lines_above = lines_above[1:LINES_ABOVE+1]
        for pattern in patterns:
            if re.search(pattern, line):
                snippet = Snippet(lines_above, line)
                snippets_queue.push(snippet)
        snippets_queue.add(line)

    pass

def main():
    parser = argparse.ArgumentParser(description=\
    """
        Parse file[s]\n\n
        examlpe: ./direlog.py file[s]
    """, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('file', nargs='+', default=[],
                        help='file[s] to do some work')
    parser.add_argument('--snippets', action='store_const', const=True)
    args = parser.parse_args()

    def input_stream_generator(): return fileinput.input(args.file)

    # for line in input_stream_generator():
        # sys.stdout.write(line)
    show_snippets(input_stream_generator())

    pass

if __name__ == '__main__':
    main()
