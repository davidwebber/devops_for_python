import unittest
import dict_cache as example

import random
import string

class Test_example_A(unittest.TestCase):
    def test_set(self):
        """
        Test that it can set a value
        """
        k = random.choice(string.ascii_letters)
        v = random.choice(range(100))
        result, success = example.set_value(k,v)
        self.assertEqual(result, v)
        self.assertEqual(success, True)

    def test_get(self):
        """
        Test that it can get a value
        """
        k = random.choice(string.ascii_letters)
        v = random.choice(range(100))
        result, success = example.set_value(k,v)
        self.assertEqual(result, v)
        self.assertEqual(success, True)
        result, success = example.get_value(k)
        self.assertEqual(result, v)
        self.assertEqual(success, True)

    def test_miss(self):
        """
        Test that a value not found yields success == False
        """
        k = ''.join(random.sample(string.ascii_letters,2))
        result, success = example.get_value(k)
        self.assertIsNone(result)
        self.assertEqual(success, True)

if __name__ == '__main__':
    unittest.main()

