import unittest

from main import ToBeTested


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        print("Start the test")

    def test_equal(self):
        self.assertEqual(ToBeTested.print_number(), ToBeTested.print_number())

    def tearDown(self) -> None:
        print("Ending the test")
