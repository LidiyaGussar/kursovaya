import unittest
from utils import mask_account
import json


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.file_path = "D:\\kursovaya\\scr\\operation.json"
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def tearDown(self) -> None:
        pass

    def test_mask_account(self):
        self.assertEqual(mask_account(), 'Visa Classic 284287******9012')

    def test_mask_account_empty_input(self):
        self.assertEqual(mask_account(''), ' ****** ')

    if __name__ == '__main__':
        unittest.main()
