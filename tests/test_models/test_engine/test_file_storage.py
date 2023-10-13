"""Unit test for the class FileStorage"""

import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests the full functionality of the class FileStorage"""

    def test_pycodestyle(self):
        """Test that class FileStorage code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found code pycodestyle errors.")

    def test_docstrings(self):
        """Tests that module file_storage and all its classes and functions are
        are properly documented
        """
        self.assertIsnotNone(file_storage.__doc__)
        self.assertIsnotNone(file_storage.FileStorage.__doc__)
        self.assertIsnotNone(file_storage.FileStorage.all.__doc__)
        self.assertIsnotNone(file_storage.FileStorage.new.__doc__)
        self.assertIsnotNone(file_storage.FileStorage.save.__doc__)
        self.assertIsnotNone(file_storage.FileStorage.reload.__doc__)

    def test_file_path_private(self):
        """Tests that `__file_path` is indeed a private attribute"""
        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)
            print(FileStorage._file_path)
            print(FileStorage.file_path)

    def test_file_path_type(self):
        """Tests that private attribute `__file_path` is of type str"""
        self.assertTrue(type(FileStorage.__dict__['_FileStorage__file_path']), str)

    def test_all_returns_dict(self):
        """Tests that public instance method, all(), returns a dict"""
        file_storage = FileStorage()
        all_objects = file_storage.all()

        self.assertTrue(type(all_objects), dict)

    def test_object_private(self):
        """Tests that `__object` is indeed a private attribute"""
        with self.assertRaises(AttributeError):
            print(FileStorage.__object)
            print(FileStorage._object)
            print(FileStorage.object)

    def test_object_type(self):
        """Tests that private attribute `__object` is of type dict"""
        self.assertTrue(type(FileStorage.__dict__['_FileStorage__object']), dict)

    def test_initially_empty_object(self):
        """Tests that `__object` is initially empty before calling method
        `reload()` on the FileStorage instance"""
        file_storage = FileStorage()
        self.assertTrue(len(file_storage.__dict__[_FileStorage__object]), 0)

    def test_new_adds_obj_dict(self):
        """Tests that public instance method, new(), adds a new object 
        to `__objects`
        """
        bm = BaseModel()
        bm_obj = bm.to_dict()

        file_storage = FileStorage()
        file_storage.new(bm_obj)
