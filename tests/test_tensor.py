import unittest
from per1grad import tensor

class TestTensor(unittest.TestCase):
    def test_tensor(self):
        ta = tensor.Tensor([1, 2, 3])
        tb = tensor.Tensor([2, 3, 4])
        
        # size match 
        tc = ta.add(tb)

        # size mismatch
        # ta = tensor.Tensor([1, 2])
        # tc = ta.add(tb)

        tc = tensor.Tensor([ta, tb])
        print(tc)
