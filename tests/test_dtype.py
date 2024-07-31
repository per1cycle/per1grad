import unittest
from per1grad import dtype

class TestDType(unittest.TestCase):
    def test_type_repr(self):
        # List of data types to test with their expected repr outputs
        types = [
            (dtype.dtypes.bool, "dtype.bool"),
            (dtype.dtypes.int8, "dtype.int8"),
            (dtype.dtypes.uint8, "dtype.uint8"),
            (dtype.dtypes.int16, "dtype.int16"),
            (dtype.dtypes.uint16, "dtype.uint16"),
            (dtype.dtypes.float16, "dtype.float16"),
            (dtype.dtypes.int32, "dtype.int32"),
            (dtype.dtypes.uint32, "dtype.uint32"),
            (dtype.dtypes.float32, "dtype.float32"),
            (dtype.dtypes.float, "dtype.float32"),
            (dtype.dtypes.int64, "dtype.int64"),
            (dtype.dtypes.uint64, "dtype.uint64"),
            (dtype.dtypes.float64, "dtype.float64"),
            (dtype.dtypes.double, "dtype.float64")
        ]

        for dtype_instance, expected_repr in types:
            self.assertEqual(dtype_instance.__repr__(), expected_repr)

    def test_from_np(self):
        
        pass 
