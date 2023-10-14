"""Unit test for the class FileStorage"""

import os
import json
import unittest
import pycodestyle
from models.engine import file_storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests the full functionality of the class FileStorage"""

    def test_pycodestyle(self):
        """Test that class FileStorage code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code pycodestyle errors.")

    def test_docstrings(self):
        """Tests that module file_storage and all its classes and functions are
        are properly documented
        """
        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.all.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.new.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.save.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.reload.__doc__)

    def test_file_path_private(self):
        """Tests that `__file_path` is indeed a private attribute"""
        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)
            print(FileStorage._file_path)
            print(FileStorage.file_path)

    def test_file_path_type(self):
        """Tests that private attribute `__file_path` is of type str"""
        self.assertTrue(type(FileStorage._FileStorage__file_path), str)

    def test_object_private(self):
        """Tests that `__object` is indeed a private attribute"""
        with self.assertRaises(AttributeError):
            print(FileStorage.__objects)
            print(FileStorage._objects)
            print(FileStorage.objects)

    def test_object_type(self):
        """Tests that private attribute `__object` is of type dict"""
        self.assertTrue(type(FileStorage._FileStorage__objects), dict)

    def test_initially_empty_object(self):
        """Tests that `__object` is initially empty before calling method
        `reload()` on the FileStorage instance"""
        file_storage = FileStorage()
        self.assertEqual(len(file_storage.all()), 0)

    def test_method_all_returns_dict(self):
        """Tests that public instance method, all(), returns a dict"""
        file_storage = FileStorage()
        all_objects = file_storage.all()

        self.assertTrue(type(all_objects), dict)

    def test_method_all_return_value(self):
        """Tests that the return value of `all()` is actually `__objects`"""
        file_storage = FileStorage()
        all_objects = file_storage.all()
        self.assertIs(file_storage._FileStorage__objects, all_objects)

    def test_method_new_adds_obj_dict(self):
        """Tests that public instance method, new(), adds a new object
        to `__objects`, and confirms the key/value format
        """
        file_storage = FileStorage()
        objs_dict = file_storage.all()
        dict_len = len(objs_dict)

        bm = BaseModel()
        bm_key = f"{bm.__class__.__name__}.{bm.id}"

        last_added_obj = objs_dict.copy().popitem()

        self.assertEqual(len(objs_dict), dict_len + 1)
        self.assertEqual(last_added_obj[0], bm_key)
        self.assertEqual(last_added_obj[1], bm.to_dict())

    def test_method_save(self):
        """Tests that the public instance method `save()` sends the JSON
        format of `__objects` to the file in the attribute `__file_path`"""
        json_file = FileStorage._FileStorage__file_path

        bm1 = BaseModel()
        bm1_key = f"{bm1.__class__.__name__}.{bm1.id}"

        bm2 = BaseModel()
        bm2_key = f"{bm2.__class__.__name__}.{bm2.id}"

        file_storage = FileStorage()
        objs_dict = file_storage._FileStorage__objects

        file_storage.new(bm1)
        file_storage.save()

        with open(json_file, "r") as file:
            objs = file.read()

        self.assertTrue(type(objs), str)
        self.assertEqual(objs, json.dumps(objs_dict))
