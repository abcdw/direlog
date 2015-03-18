# -*- coding: utf-8 -*-
import re

pre_patterns = [
    (
        r'(\d{16}-[-\w]*\b)',
        r'REQUEST_ID_SUBSTITUTE',
    ),
    (
        # r'([\dA-F]){8}-[\dA-F]{4}-4[\dA-F]{3}-[89AB][\dA-F]{3}-[\dA-F]{12}',
        r'([0-9A-F]){8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}',
        # r'[0-9A-F-]{36}',
        # r'ACE088EB-ECA6-4348-905A-041EF10DBD53',
        r'UUID_SUBSTITUTE',
    ),
]
