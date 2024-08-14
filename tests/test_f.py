import unittest

from torch.functional import F 

class TestF(unittest.TestCase):
    def test_op(self):
        print(F)