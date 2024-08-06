
import numpy as np
from per1grad.buffer import Buffer
from per1grad.ops import Ops
class Function:
    def __init__(self):
        pass 
    def forward(self): 
        raise NotImplementedError("forward is not used in base class")
    def backward(self):
        raise NotImplementedError("backward is not used in base class")
    @staticmethod
    def relu(x: Buffer) -> Buffer:
        return x.doop(Ops.MAX, Buffer(np.zeros_like(x.base()._np)))
    @staticmethod
    def sigmoid(x: Buffer):
        return 1 / (1 + np.exp(np.negative(x._np)))


