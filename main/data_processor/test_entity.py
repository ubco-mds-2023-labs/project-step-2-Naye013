import unittest
import numpy as np
from scipy.stats import mode
from entity import Entity, EntityCollection

class TestEntity(unittest.TestCase):

    # Test to check whether the attributes a new Entity instance match the expected values
    def test_entity_creation(self):
        entity = Entity("1", {"field1": 10})
        self.assertEqual(entity.entity_id, "1")
        self.assertEqual(entity.field_value_pairs, {"field1": 10})

    # Test to add key-value pairs to the attributes from an entity
    def test_add_field(self):
        entity = Entity("1")
        entity.add("field1", 20)
        self.assertEqual(entity.field_value_pairs, {"field1": 20})

    # Test to skip adding non-numeric values in a field
    def test_add_non_numeric_field(self):
        entity = Entity("1")
        entity.add("field1", "abc")
        self.assertEqual(entity.field_value_pairs, {})

class TestEntityCollection(unittest.TestCase):

    # Test to check that an entity is added to the collection and the returned entity refer to the same underlying object.
    def test_add_entity(self):
        collection = EntityCollection()
        entity = collection.add_entity("1")
        self.assertEqual(len(collection.items), 1)
        self.assertIs(collection.items[0], entity)

    def test_compute_mean(self):
        collection = EntityCollection()
        collection.add("1", {"score": 10})
        collection.add("2", {"score": 20})
        self.assertEqual(collection.compute_mean("score"), 15.0)

    def test_compute_mode(self):
        collection = EntityCollection()
        collection.add("1", {"score": 10})
        collection.add("2", {"score": 20})
        self.assertEqual(collection.compute_mode("score"), 10)

    def test_compute_median(self):
        collection = EntityCollection()
        collection.add("1", {"score": 10})
        collection.add("2", {"score": 20})
        self.assertEqual(collection.compute_median("score"), 15.0)

    def test_compute_min(self):
        collection = EntityCollection()
        collection.add("1", {"score": 10})
        collection.add("2", {"score": 20})
        self.assertEqual(collection.compute_min("score"), 10)

    def test_compute_max(self):
        collection = EntityCollection()
        collection.add("1", {"score": 10})
        collection.add("2", {"score": 20})
        self.assertEqual(collection.compute_max("score"), 20)

    def test_compute_count(self):
        collection = EntityCollection()
        collection.add("1", {"score": 10})
        collection.add("2", {"score": 20})
        self.assertEqual(collection.compute_count("score"), 2)

unittest.main(argv=[''], verbosity=2, exit=False)
