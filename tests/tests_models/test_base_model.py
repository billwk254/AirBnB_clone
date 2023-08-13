"""
This module contains unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """

    def test_id_attribute(self):
        """
        Test if the id attribute is present and is a string.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertIsInstance(my_model.id, str)

    def test_created_at_attribute(self):
        """
        Test if the created_at attribute is present and is a datetime object.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at_attribute(self):
        """
        Test if the updated_at attribute is present and is a datetime object.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save_method(self):
        """
        Test if the save method updates the updated_at attribute.
        """
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dictionary with the required attributes.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()

        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertIn('__class__', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)

    def test_to_dict_datetime_format(self):
        """
        Test if the to_dict method returns datetime attributes in the correct format.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()

        created_at = datetime.strptime(my_model_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.strptime(my_model_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

        self.assertEqual(created_at, my_model.created_at)
        self.assertEqual(updated_at, my_model.updated_at)

    def test_to_dict_custom_attributes(self):
        """
        Test if the to_dict method includes custom attributes.
        """
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        my_model_dict = my_model.to_dict()

        self.assertIn('name', my_model_dict)
        self.assertIn('my_number', my_model_dict)
        self.assertEqual(my_model_dict['name'], "Test Model")
        self.assertEqual(my_model_dict['my_number'], 42)

    def test_init_with_kwargs(self):
        """
        Test if an instance can be re-created from its dictionary representation.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)

        self.assertEqual(new_model.id, my_model.id)
        self.assertEqual(new_model.created_at, my_model.created_at)
        self.assertEqual(new_model.updated_at, my_model.updated_at)

    def test_str_representation(self):
        """
        Test if the string representation of BaseModel is as expected.
        """
        my_model = BaseModel()
        str_representation = str(my_model)
        expected = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str_representation, expected)

if __name__ == '__main__':
    unittest.main()

