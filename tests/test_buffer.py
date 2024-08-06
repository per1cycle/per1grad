import unittest
from per1grad.buffer import Buffer
import numpy as np 


class TestDType(unittest.TestCase):
    def test_buffer_0x0(self):
        a = np.array([])
        b = np.array([])
        ba = Buffer(a)
        bb = Buffer(b)
        c = np.array([a, b])
        bc = Buffer([ba, bb])
        self.assertEqual(c.shape, bc._np.shape)
        
    def test_buffer_2x2(self):
        a = np.array([1, 2])
        b = np.array([2, 3])
        ba = Buffer(a)
        bb = Buffer(b)
        c = np.array([a, b])
        bc = Buffer([ba, bb])
        self.assertEqual(c.shape, bc._np.shape)

    def test_buffer_2x2x2(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[4, 5], [5, 6]])
        ba = Buffer(a)
        bb = Buffer(b)
        c = np.array([a, b])
        bc = Buffer([ba, bb])
        self.assertEqual(c.shape, bc._np.shape)


        
