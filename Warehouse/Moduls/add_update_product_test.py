import unittest


class TestUniqID(unittest.TestCase):

    def setUpClass(self) -> None:
        print("Start the test")

    def test_equal(self):
        self.assertTrue(self.get_product_name_from_user())

    def tearDown(self) -> None:
        print("Ending the test")
