from enum import Enum, auto

class Ops(Enum):
    # unary ops
    NOOP = auto()
    EXP2 = auto()
    LOG2 = auto()
    CAST = auto()
    SIN = auto()
    SQRT = auto()
    NEG = auto()

    # binary op +-/*
    ADD = auto()
    SUB = auto()
    DIV = auto()
    MUL = auto()
    MOD = auto()

class Device():
    pass 

