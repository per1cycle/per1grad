from __future__ import annotations

import numpy as np 
class Tensor:
    """
        Tensor usage in v0.0.1-alpha:
        >>> 
    """
    def __init__(self, data, require_grad: bool= False) -> None:
        
        if isinstance(data, list):
            self.data = np.array([d.data if isinstance(d, Tensor) else d for d in data])
            self.require_grad = require_grad

        elif isinstance(data, (int, float)) :
            self.data = np.array(data)
            self.require_grad = require_grad
        elif isinstance(data, np.ndarray):
            self.data = data
            self.require_grad = require_grad
        else :
            raise NotImplementedError("Other datatype is not implemented yet.")
        
    def __repr__(self) -> str:
        return f"<per1grad Tensor: data: \n{self.data},\nnrequire_grad: {self.require_grad}>"
    
    def add(self, tensor: Tensor):
        if self.data.shape != tensor.data.shape:
            raise TypeError("Shape not match")
        return Tensor(self.data + tensor.data)
    
    def sub(self, tensor: Tensor):
        if self.data.shape != tensor.data.shape:
            raise TypeError("Shape not match")
        return Tensor(self.data - tensor.data)
    
    def mul(self, tensor: Tensor):
        if self.data.shape != tensor.data.shape:
            raise TypeError("Shape not match")
        return Tensor(self.data * tensor.data)
    
    def pow(self, powval):
        pass 
