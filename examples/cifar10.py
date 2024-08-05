from per1grad import helper
from per1grad.tensor import Tensor

class Per1Net(Tensor):
    def __init__(self):
        super.__init__()
    
    def forward(self, x):
        pass 

def train(x_train, y_train, net: Tensor)->None:
    pass 


if __name__ == "__main__":
    x_train, y_train, x_test, y_test = helper.load_cifar()
    model = Per1Net()