from enum import Enum, auto

class Ops(Enum):
    # unary ops
    NOOP = auto()
    EXP = auto()
    LOG = auto()
    CAST = auto()
    SIN = auto()
    SQRT = auto()
    NEG = auto()

    # binary op +-/*
    ADD = auto()
    SUB = auto()
    DIV = auto()
    LMUL = auto()
    RMUL = auto()
    MOD = auto()
    MAX = auto()

