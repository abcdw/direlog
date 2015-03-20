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
    (
        # r"""
        # (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
        # (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
        # (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
        # (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
        # """,
        # r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
        r'\b(\d{1,3}\.){3}\d{1,3}\b',
        r'IP_ADDRESS_SUBSTITUTE',
    ),
    (
        r'js:\d+:\d+',
        r'js:POSITION_SUBSTITUTE',
    ),
    (
        r'line \d+',
        r'LINE_SUBSTITUTE',
    ),
    (
        r'\w{3} \w{3} \d{1,2} \d{1,2}:\d{1,2}:\d{1,2} \d{4}',
        r'TIMESTAMP_SUBSTITUTE',
    ),
]
