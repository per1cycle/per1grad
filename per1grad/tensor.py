from __future__ import annotations

from per1grad.buffer import Buffer
from __init__ import __version__

class Tensor:
    
    def __init__(self, data, need_grad: bool= True) -> None:
        if isinstance(data, list):
            self.data = [ Tensor(d, need_grad) for d in data ]
            self.need_grad = need_grad
        elif isinstance(data, (int, float)) :
            self.need_grad = need_grad
        else :
            raise RuntimeError(f"Other type is not support in per1grad v-{__version__}")
    def __repr__(self) -> str:
        return f"<per1grad Tensor: data {self.data}, need_grad: {self.need_grad}>"
    
