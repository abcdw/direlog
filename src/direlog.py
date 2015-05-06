#!/usr/bin/env python
# encoding: utf-8

import sys
import re
import argparse
import fileinput
import copy
import itertools

from argparse import RawDescriptionHelpFormatter

from patterns import main_patterns


BUFFER_SIZE = 30

class Buffer(object):
    """Class for buffering input"""

    def __init__(self):
        self.buf = [''] * BUFFER_SIZE
        self.line_scrolled = 0

    def add(self, line):
        self.buf.append(line)
        self.buf = self.buf[1:BUFFER_SIZE+1]
        self.line_scrolled += 1

    def text(self):
        """Return joined lines
        :returns: str()

        """
        return ''.join(self.buf)


def make_escaped(string):
    """Make escaped pattern from string

    :string: string to be escaped
    :returns: pattern

    """

    return re.escape(string.replace('\n', 'NSLPH')).replace('NSLPH', '\n') + r'\n\Z'


def show_stat(input_stream, snippets_count=0, context=3,
              patterns=main_patterns,
              output_stream=sys.stdout, snippets_file=None):
    """Show statistics for patterns

    :input_stream: input stream
    :snippets_count: maximum number of snippets to show for every pattern
    :context: number of lines in snippet around last line of pattern match
    :patterns: patterns that need to look
    :output_stream: stream for output
    :returns: None

    """

    LINES_ABOVE = context
    LINES_BELOW = context
    SNIPPETS_TO_SHOW = snippets_count
    SHOW_SNIPPETS = snippets_count > 0

    class Snippet(object):
        def __init__(self, lines_above, pattern, line_number):
            self.text = copy.copy(lines_above)
            self.pattern = pattern
            self.line_number = line_number

        def full(self):
            return len(self.text) >= LINES_ABOVE + LINES_BELOW + 1

        def add(self, line):
            self.text.append(line)

        def show(self):
            i = 0
            for line in self.text:
                if i == LINES_ABOVE:
                    output_stream.write('| {} ==>'.format(self.line_number))
                else:
                    if re.search(self.pattern, line):
                        output_stream.write('|-->')
                    else:
                        output_stream.write('|>')
                output_stream.write(line)
                i += 1


    class SnippetsQueue(object):
        def __init__(self):
            self.new_snippets = []
            self.ready_snippets = {}
            self.pattern_used = {}

        def push(self, snippet):
            if not self.pattern_used.get(pattern, False):
                self.new_snippets.append(snippet)
            self.pattern_used[pattern] = True

        def add(self, line):
            for snippet in self.new_snippets:
                if snippet.full():
                    self.make_ready(snippet)
                else:
                    snippet.add(line)

        def make_ready(self, snippet):
            self.new_snippets.remove(snippet)
            pattern = snippet.pattern
            try:
                self.ready_snippets[pattern].append(snippet)
            except KeyError:
                self.ready_snippets[pattern] = [snippet]
            self.pattern_used[pattern] = False
            if len(self.ready_snippets[pattern]) == SNIPPETS_TO_SHOW:
                self.pattern_used[pattern] = True

        def make_all_ready(self):
            for snippet in self.new_snippets:
                self.make_ready(snippet)


    class StatCollector(object):

        """Class for collecting statistics"""

        def __init__(self):
            self.match_count = {}
            pass

        def add(self, pattern):
            """Add pattern matching event"""
            if pattern not in self.match_count:
                self.match_count[pattern] = 0
            self.match_count[pattern] += 1


    def print_stat(stat_collector, snippets_queue=None):

        """Print statistics and snippets"""

        for pattern, count in stat_collector.match_count.iteritems():
            print """\
********************************************************************************
pattern: "{}"
--------------------------------------------------------------------------------
number of matches: {}
********************************************************************************\
""".format(pattern, count)
            if snippets_queue:
                if pattern in snippets_queue.ready_snippets:
                    for snippet in snippets_queue.ready_snippets[pattern]:
                        snippet.show()
                        output_stream.write('-' * 80 + '\n')
                else:
                    output_stream.write('|No snippets found : (\n')
                    output_stream.write('-' * 80 + '\n')


    stat_collector = StatCollector()
    snippets_queue = SnippetsQueue()
    line_number = 1
    input_buffer = Buffer()
    if snippets_file:
        snippets_buffer = Buffer()
    else:
        snippets_buffer = input_buffer

    for line in input_stream:
        input_buffer.add(line)
        if snippets_file:
            line = snippets_file.readline()
            snippets_buffer.add(line)

        for pattern in patterns:
            text = input_buffer.text()
            if re.search(pattern, text):
                if SHOW_SNIPPETS:
                    if LINES_ABOVE > 0:
                        snippet_begining = snippets_buffer.buf[-LINES_ABOVE:]
                    else:
                        snippet_begining = []

                    snippet = Snippet(snippet_begining, pattern,
                                      line_number)
                    snippets_queue.push(snippet)
                stat_collector.add(pattern)

        snippets_queue.add(line)
        line_number += 1

    snippets_queue.make_all_ready()
    if not SHOW_SNIPPETS:
        snippets_queue = None
    print_stat(stat_collector, snippets_queue)


def show_patterns():
    """Show patterns from patterns.py"""

    for pattern in main_patterns:
        print pattern
        print '-' * 80


def main():
    parser = argparse.ArgumentParser(description=\
    """
        Parse file[s]\n\n
        examlpe: ./direlog.py file[s] -s 2 -C 3
    """, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('file', nargs='*', default=[],
                        help='file[s] to be parsed')
    parser.add_argument('-s', '--snippets', nargs='?', type=int, const=5,
                        help='show maximum SNIPPETS snippets (5 default)')
    parser.add_argument('-C', '--context', nargs='?', type=int,
                        help='show CONTEXT lines around pattern last line')
    parser.add_argument('-p', '--patterns', action='store_const', const=True,
                        help='show patterns')
    parser.add_argument('-e', '--escape', action='store_const', const=True,
                        help='escape given string')
    parser.add_argument('--original', nargs=1,
                        help='provide original file for better snippets')

    args = parser.parse_args()
    # args = parser.parse_args(['error_log.prep', '-s', '2',
                              # '--original', 'error_log'])

    def input_stream_generator(): return fileinput.input(args.file)

    if args.patterns:
        show_patterns()
        return

    if args.escape:
        text = ''
        for line in input_stream_generator():
            text += line
        escaped_text = make_escaped(text)
        print '\n'
        print escaped_text
        return

    kwargs = {}
    if args.snippets:
        kwargs['snippets_count'] = args.snippets

    if args.context is not None:
        kwargs['context'] = args.context

    if args.original:
        kwargs['snippets_file'] = fileinput.input(args.original)

    show_stat(input_stream_generator(), **kwargs)


if __name__ == '__main__':
    main()
