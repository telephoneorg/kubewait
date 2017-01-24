"""
KubeWait UnitTests
~~~~~~~~~~~~~
"""

import os
import sys
import unittest


class TestCase(unittest.TestCase):
    """
    Parent class for all unittests.
    """
    pass


sys.path.insert(0, os.path.abspath('..'))
