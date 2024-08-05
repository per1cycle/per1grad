import numpy as np 

class Buffer:
    def __init__(self, x: np.ndarray) -> None:
        self._x = x
    
    def reshape(self, arg):
        return Buffer(np.reshape(self._x, arg))
    