"""
Tests for the Citizen entity.

Run with:
    cd simulation
    python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

# Make `src` importable when running this file directly or via
# `unittest discover` from the `simulation/` folder, without needing the
# package to be pip-installed.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.entities.citizen import Citizen, EducationLevel


class TestCitizenBasics(unittest.TestCase):
    def test_creation_sets_basic_fields(self):
        c = Citizen(name="Asha", age=25, gender="female")
        self.assertEqual(c.name, "Asha")
        self.assertEqual(c.age, 25)
        self.assertEqual(c.gender, "female")

    def test_defaults_are_sensible(self):
        c = Citizen(name="Asha", age=25, gender="female")
        self.assertIsNone(c.occupation)
        self.assertEqual(c.income, 0.0)
        self.assertEqual(c.education_level, EducationLevel.NONE)
        self.assertEqual(c.cultural_knowledge, {})
        self.assertEqual(c.children_ids, [])

    def test_each_citizen_gets_a_unique_id(self):
        c1 = Citizen(name="A", age=20, gender="male")
        c2 = Citizen(name="B", age=22, gender="female")
        self.assertNotEqual(c1.id, c2.id)


class TestCitizenLifeStatus(unittest.TestCase):
    def test_is_adult(self):
        child = Citizen(name="Kid", age=10, gender="male")
        adult = Citizen(name="Grownup", age=30, gender="female")
        self.assertFalse(child.is_adult())
        self.assertTrue(adult.is_adult())

    def test_is_adult_custom_age(self):
        teen = Citizen(name="Teen", age=16, gender="male")
        self.assertFalse(teen.is_adult(adult_age=18))
        self.assertTrue(teen.is_adult(adult_age=15))

    def test_is_employed(self):
        c = Citizen(name="Rahul", age=30, gender="male")
        self.assertFalse(c.is_employed())
        c.occupation = "Weaver"
        self.assertTrue(c.is_employed())


class TestCitizenCulturalKnowledge(unittest.TestCase):
    def test_starts_knowing_no_traditions(self):
        c = Citizen(name="Meera", age=15, gender="female")
        self.assertFalse(c.knows_tradition("madhubani_painting"))
        self.assertEqual(c.knowledge_of("madhubani_painting"), 0.0)

    def test_learn_tradition_increases_knowledge(self):
        c = Citizen(name="Meera", age=15, gender="female")
        c.learn_tradition("madhubani_painting", 20)
        self.assertEqual(c.knowledge_of("madhubani_painting"), 20)
        self.assertTrue(c.knows_tradition("madhubani_painting"))

    def test_learn_tradition_is_cumulative(self):
        c = Citizen(name="Meera", age=15, gender="female")
        c.learn_tradition("madhubani_painting", 20)
        c.learn_tradition("madhubani_painting", 15)
        self.assertEqual(c.knowledge_of("madhubani_painting"), 35)

    def test_learn_tradition_caps_at_100(self):
        c = Citizen(name="Meera", age=15, gender="female")
        c.learn_tradition("madhubani_painting", 90)
        c.learn_tradition("madhubani_painting", 90)
        self.assertEqual(c.knowledge_of("madhubani_painting"), 100)

    def test_learn_tradition_rejects_negative_amount(self):
        c = Citizen(name="Dev", age=15, gender="male")
        with self.assertRaises(ValueError):
            c.learn_tradition("kathak", -5)


class TestCitizenFamily(unittest.TestCase):
    def test_add_child_links_family(self):
        parent = Citizen(name="Mother", age=40, gender="female")
        parent.add_child(101)
        self.assertEqual(parent.children_ids, [101])

    def test_add_child_does_not_duplicate(self):
        parent = Citizen(name="Mother", age=40, gender="female")
        parent.add_child(101)
        parent.add_child(101)
        self.assertEqual(parent.children_ids, [101])


if __name__ == "__main__":
    unittest.main()
