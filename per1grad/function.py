
import numpy as np
from per1grad.buffer import Buffer
from per1grad.ops import Ops

class Function:
    """
        usage: 
        >>> from per1grad import function as F
        >>> t = Tensor()
        >>> F.relu()
    """
    def __init__(self):
        pass 
    @staticmethod
    def forward(self): 
        raise NotImplementedError("forward is not support in base class")
    @staticmethod
    def backward(self):
        raise NotImplementedError("backward is not support in base class")

class ReLU(Function):
    def __init__(self):
        super().__init__()

    def forward():
        pass 


