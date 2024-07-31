import numpy as np 
from dataclasses import dataclass
from typing import Final, Optional

@dataclass 
class DType:
    priority: int
    item_size: int # eg: int for 4bytes, char for 1byte.
    name: str 
    data: Optional[type]

    def __repr__(self) -> str:
        return f"dtype.{self.name}"
    
class dtypes:
    @staticmethod
    def is_int(x: DType)-> bool: 
        return x in [
            dtypes.int8,
            dtypes.int16,
            dtypes.int32,
            dtypes.int64,
            dtypes.uint8,
            dtypes.uint16,
            dtypes.uint32,
            dtypes.uint64,
            ]
    @staticmethod
    def is_float(x: DType)->bool:
        return x in [
            dtypes.float16,
            dtypes.float32,
            dtypes.float64,
        ]
    @staticmethod
    def is_uint(x: DType)-> bool: 
        return x in [
            dtypes.uint8,
            dtypes.uint16,
            dtypes.uint32,
            dtypes.uint64,
            ]
    @staticmethod
    def to_np(x: DType)-> bool :
        # todo
        return True
    @staticmethod
    def from_np(x: np.dtype)-> DType:
        return DTYPE_DICT[np.dtype(x).name]
    bool: Final[DType] = DType(0, 1, "bool8", np.bool8)
    int8: Final[DType] = DType(1, 1, "int8", np.int8)
    uint8: Final[DType] = DType(2, 1, "uint8", np.uint8)

    int16: Final[DType] = DType(3, 2, "int16", np.int16)
    uint16: Final[DType] = DType(4, 2, "uint16", np.uint16)
    float16: Final[DType] = DType(5, 2, "float16", np.float16)

    int32: Final[DType] = DType(6, 4, "int32", np.int32)
    uint32: Final[DType] = DType(7, 4, "uint32", np.uint32)
    float32: Final[DType] = DType(8, 4, "float32", np.float32)
    float = float32

    int64: Final[DType] = DType(9, 8, "int64", np.int64)
    uint64: Final[DType] = DType(10, 8, "uint64", np.uint64)
    float64: Final[DType] = DType(11, 8, "float64", np.float64)
    double = float64

DTYPE_DICT = {k: v for k, v in dtypes.__dict__.items() if not k.startswith("__") and v.__class__ is not staticmethod }

