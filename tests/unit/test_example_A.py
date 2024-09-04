import unittest
import example_A as example

import random
import string

class Test_example_A(unittest.TestCase):
    def test_set(self):
        """
        Test that it can set a value
        """
        k = random.choice(string.ascii_letters)
        v = random.choice(range(100))
        result, err = example.set_value(k,v)
        self.assertEqual(result, v)
        self.assertIsNone(err)

    def test_get(self):
        """
        Test that it can get a value
        """
        k = random.choice(string.ascii_letters)
        v = random.choice(range(100))
        result, err = example.set_value(k,v)
        self.assertEqual(result, v)
        result, err = example.get_value(k)
        self.assertEqual(result, v)
        self.assertIsNone(err)

if __name__ == '__main__':
    unittest.main()

