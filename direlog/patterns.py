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
    (
        r"'0x[a-f0-9]{7}'",
        r"'AJAX_VERSION_SUBSTITUTE'",
    ),
    (
        r'-\d{3}-\d{10}',
        r'-SHARD_SUBSTITUTE',
    ),
]

main_patterns = [
    r'Expected\ an\ even\-sized\ list\ of\ pairs\ \(k1\,\ v1\,\ \.\.\.\ kN\,\ vN\)\,\ got\ \(p0\)\n\Z',

    r'Names\ not\ in\ dictionary\:.*\n\Z',

    r"""JavaScript\.\ TypeError\:\ Object\ \#\<t\>\ has\ no\ method\ \'Ukraine\'
\ \ \ \ at\ Object\.blocks\.b\-counters\_\_gemius\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ Object\.\[object\ Function\]\.Object\.toString\.call\.e\.\(anonymous\ function\)\ \[as\ b\-counters\_\_gemius\]\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ Object\.blocks\.b\-counters\.blocks\.b\-cntrs\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ Object\.\[object\ Function\]\.Object\.toString\.call\.e\.\(anonymous\ function\)\ \[as\ b\-counters\]\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ Object\.blocks\.b\-page\_\_content\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ Object\.blocks\.b\-page\_\_content\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ Object\.\[object\ Function\]\.Object\.toString\.call\.e\.\(anonymous\ function\)\ \[as\ b\-page\_\_content\]\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ blocks\.b\-page\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ Object\.blocks\.b\-page\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)
\ \ \ \ at\ Object\.\[object\ Function\]\.Object\.toString\.call\.e\.\(anonymous\ function\)\ \[as\ b\-page\]\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)\ at\ \/db\/BASE\/upper\-SHARD\_SUBSTITUTE\/arkanavt\/report\/lib\/YxWeb\/Util\/Template\/JS\.pm\ LINE\_SUBSTITUTE\.\ \(Object\.blocks\.b\-page\ \(web3\_exp\/pages\-desktop\/search\/\_search\.all\.priv\.js\:POSITION\_SUBSTITUTE\)\)\n\Z""",

    r'No\ ajax\ static\ version\ \'AJAX\_VERSION\_SUBSTITUTE\'\.\ Found\:\ \'AJAX\_VERSION\_SUBSTITUTE\'\ at\ \/db\/BASE\/upper-SHARD\_SUBSTITUTE\/arkanavt\/report\/lib\/YxWeb\/Handler\.pm\ LINE\_SUBSTITUTE\.\n\Z',

    r'RecodeToUnicode\ failed\ at\ \/db\/BASE\/upper-SHARD\_SUBSTITUTE\/arkanavt\/report\/lib\/YxWeb\/Util\/Words\.pm\ LINE\_SUBSTITUTE\.\n\Z',

    r'not\ found\ snippet\ for\ spec\_type\ \'.*\'\ in\ \_ReportSnipAttrs\ at\ \/db\/BASE\/upper-SHARD\_SUBSTITUTE\/arkanavt\/report\/lib\/YxWeb\/Module\/Snippet\/List\.pm\ LINE\_SUBSTITUTE\.\n\Z',
]
