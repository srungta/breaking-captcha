import os
import random
import string
import unittest
from pre_process import file_helper

class FileHelperTest(unittest.TestCase):
    def test_folder_creation(self):
        file_helper.create_folder(self.unique_folder_path)
        self.assertTrue(os.path.exists(self.unique_folder_path))

    def test_file_creation(self):
        file_helper.create_folder(self.unique_folder_path)
        file_helper.create_file(self.unique_file_path)
        self.assertTrue(os.path.isfile(self.unique_file_path))

    def test_get_filenames_from_folder(self):
        file_helper.create_folder(self.unique_folder_path)
        file_helper.create_file(self.unique_file_path)
        filenames = file_helper.get_filenames_from_folder(self.unique_folder_path)
        self.assertEqual(len(filenames), 1)

    def test_copy_file(self):
        file_helper.create_folder(self.unique_folder_path)
        file_helper.create_file(self.unique_file_path)
        file_helper.copy_file(self.unique_file_path, self.new_file_name)
        self.assertTrue(os.path.isfile(self.new_file_name))


    @staticmethod
    def id_generator():
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(4))

    def setUp(self):
        self.unique_folder_path = "B:\\"
        self.unique_file_path = "testfile"
        while os.path.exists(self.unique_folder_path):
            self.unique_folder_path = self.unique_folder_path + FileHelperTest.id_generator()
        self.unique_file_path = self.unique_folder_path + "\\" + self.unique_file_path
        self.new_file_name = self.unique_file_path + "new"
        return super().setUp()

    def tearDown(self):
        if os.path.isfile(self.unique_file_path):
            os.remove(self.unique_file_path)
        if os.path.isfile(self.new_file_name):
            os.remove(self.new_file_name)
        if os.path.exists(self.unique_folder_path):
            os.removedirs(self.unique_folder_path)
        return super().tearDown()