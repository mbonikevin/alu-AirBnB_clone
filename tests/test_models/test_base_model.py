#!/usr/bin/python3
"""Unittest for BaseModel class."""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def test_instance(self):
        """Test object instantiation."""
        self.assertIsInstance(self.model, BaseModel)

    def test_id_is_str(self):
        """Test that id is a string."""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict_contains_keys(self):
        """Test if to_dict has correct keys."""
        model_dict = self.model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

