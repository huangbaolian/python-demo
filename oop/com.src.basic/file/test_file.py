import unittest

from file_operation import open_file

class Test(unittest.TestCase):
    def setUp(self) -> None:
        open_file()

    def test_file(self):
        var = self.assertEquals
