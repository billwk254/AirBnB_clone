"""Unittests for BaseModel class."""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines TestBaseModel class."""
    def setUp(self):
        """Set up BaseModel instance for testing."""
        self.base = BaseModel()

    def tearDown(self):
        """Clean up after each test method."""
        del self.base

    def test_base_model_attributes(self):
        """Test attributes of BaseModel."""
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str_representation(self):
        """Test __str__ method."""
        str_repr = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), str_repr)

    def test_save_method(self):
        """Test save method."""
        prev_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(prev_updated_at, self.base.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method."""
        obj_dict = self.base.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base.id)
        self.assertEqual(obj_dict['created_at'], self.base.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base.updated_at.isoformat())

    def test_dict_to_instance(self):
        """Test creating an instance from a dictionary."""
        obj_dict = self.base.to_dict()
        new_instance = BaseModel(**obj_dict)
        self.assertEqual(new_instance.id, self.base.id)
        self.assertEqual(new_instance.created_at, self.base.created_at)
        self.assertEqual(new_instance.updated_at, self.base.updated_at)

if __name__ == '__main__':
    unittest.main()
