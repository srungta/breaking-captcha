import os
import random
import string
import unittest
from pre_process import file_helper

class FileHelperTest(unittest.TestCase):
    def test_folder_creation(self):
        file_helper.create_folder(self.unique_test_path)
        self.assertTrue(os.path.exists(self.unique_test_path))

    @staticmethod
    def id_generator():
        chars=string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(4))

    def setUp(self):
        self.unique_test_path = "B:\Temp2"
        while os.path.exists(self.unique_test_path):
            self.unique_test_path = self.unique_test_path + FileHelperTest.id_generator()
        return super().setUp()
    
    def tearDown(self):
        if os.path.exists(self.unique_test_path):
            os.removedirs(self.unique_test_path)
        return super().tearDown()

