from __future__ import annotations

from per1grad.buffer import Buffer
class Tensor:
    def __init__(self, data, require_grad: bool= False) -> None:
        if isinstance(data, list):
            self.data = Buffer([Buffer(d, require_grad) for d in data ])
            self.require_grad = require_grad
        elif isinstance(data, (int, float)) :
            self.data = 
            self.require_grad = require_grad
        else :
            raise NotImplementedError("Other datatype is not implemented yet.")
        
    def __repr__(self) -> str:
        return f"<per1grad Tensor: data {self.data}, require_grad: {self.require_grad}>"
    
