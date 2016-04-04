import sys


if sys.version_info.major > 2:
    from unittest import mock
    sys.modules['mock'] = mock
