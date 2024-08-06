import unittest
from per1grad import dtype
from torch.functional import F 

class TestF(unittest.TestCase):
    def test_op(self):
        F.relu()
