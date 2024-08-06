class Module:
    def forward(self, *input):
        raise NotImplementedError

    def __call__(self, *input):
        return self.forward(*input)
