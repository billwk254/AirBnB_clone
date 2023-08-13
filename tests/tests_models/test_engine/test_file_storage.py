#!/usr/bin/python3


"""
Unittests for FileStorage class.
"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all method."""
        all_objs = self.storage.all()
        self.assertEqual(type(all_objs), dict)
        self.assertEqual(all_objs, self.storage._FileStorage__objects)

    def test_new(self):
        """Test new method."""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(type(model).__name__, model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_save_reload(self):
        """Test save and reload methods."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(type(model).__name__, model.id)
        self.assertTrue(key in new_storage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
