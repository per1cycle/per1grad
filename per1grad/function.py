

class Function:
    def __init__(self, x):
        self._x = x
    def forward(self): 
        raise NotImplementedError("forward is not used in base class")
    def backward(self):
        raise NotImplementedError("backward is not used in base class")

    def relu(self):
        pass 

    def sigmoid(self):
        pass 
    

