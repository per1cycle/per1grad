from __future__ import annotations

import numpy as np 
from per1grad.ops import Ops

class Buffer:
    def __init__(self, x: np.ndarray) -> None:
        self._np = x
    def __repr__(self) -> str:
        return f"per1grad buffer:\n {self._np}"
    def base(self): 
        return self
    def reshape(self, arg):
        return Buffer(np.reshape(self._np, arg))
    
    def doop(self, op: Ops, *src: Buffer):
        # unary op
        if op == Ops.NOOP:
            return self.base()
        elif op == Ops.EXP:
            return Buffer(np.exp(self._np))
        elif op == Ops.LOG:
            return Buffer(np.log(self._np))
        elif op == Ops.CAST:
            pass 
        elif op == Ops.SIN:
            return Buffer(np.sqrt(self._np))
        elif op == Ops.NEG:
            return Buffer(np.negative(self._np))
        
        # binary op
        elif op == Ops.ADD:
            return Buffer(self._np + src[0].base()._np)
        elif op == Ops.SUB:
            return Buffer(self._np - src[0].base()._np)
        elif op == Ops.DIV:
            return Buffer(self._np / src[0].base()._np)
        elif op == Ops.LMUL:
            return Buffer(self._np * src[0].base()._np)
        elif op == Ops.RMUL:
            return Buffer(src[0].base()._np * self.base()._np)
        elif op == Ops.MOD:
            return Buffer(self._np % src[0].base()._np)
        elif op == Ops.MAX:
            return Buffer(np.maximum(self._np, src[0].base()._np))
        
        
        
        
