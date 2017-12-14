import numpy as np
import unittest
from pre_process import distribution

class DistributionTest(unittest.TestCase):
    def test_create_data_sets(self):
        train, validate, test = distribution.create_data_sets(self.data, 70, 20, 10)
        self.assertEqual(len(train), 7)
        self.assertEqual(len(validate), 2)
        self.assertEqual(len(test), 1)

        train, validate, test = distribution.create_data_sets(self.data, 77, 13, 10)
        self.assertEqual(len(train), 8)
        self.assertEqual(len(validate), 1)
        self.assertEqual(len(test), 1)

    def test_data_partitions_should_add_to_100(self):
        try:
            train, validate, test = distribution.create_data_sets(self.data, 70, 20, 5)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        
    def setUp(self):
        self.data = np.array(['a' ,'single' ,'distinct' ,'meaningful' ,'element' ,'of' ,'speech' ,'or' ,'writing', 'hi'])
        return super().setUp()

    def tearDown(self):
        return super().tearDown()