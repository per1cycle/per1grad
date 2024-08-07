from per1grad import helper
from per1grad.tensor import Tensor
import per1grad.nn as nn 

class Per1Net:
    def __init__(self):
        self.l1 = Tensor()
    def forward(self, x):
        pass 

def train(x_train, y_train, )->None:
    pass 


if __name__ == "__main__":
    x_train, y_train, x_test, y_test = helper.load_cifar()
    model = Per1Net()
    