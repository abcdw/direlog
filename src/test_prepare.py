#!/usr/bin/env python
# encoding: utf-8

import unittest
import StringIO

from prepare import prepare


class TestSUBSTITUTION(unittest.TestCase):

    """Docstring for TestSUBSTITUTION. """

    def setUp(self):
        pass

    def test_UUID(self):
        text  = 'ACE088EB-ECA6-4348-905A-041EF10DBD53'
        text += 'AAAAAAAA-0000-FFFF-1111-999999999999'
        text += 'ACE088EB-ECA6-4348-905A-041EF10DBD53'
        text += 'ACE088EB-ECA6-4348-905A-041EF10DBDG3'

        result_text = StringIO.StringIO()
        prepare(text.split('\n'), result_text)

        reference_string  = 'UUID_SUBSTITUTE' * 3
        reference_string += 'ACE088EB-ECA6-4348-905A-041EF10DBDG3'

        self.assertEqual(result_text.getvalue(), reference_string)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSUBSTITUTION)
    unittest.TextTestRunner(verbosity=2).run(suite)
