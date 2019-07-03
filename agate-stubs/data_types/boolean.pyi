# Stubs for agate.data_types.boolean (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from agate.data_types.base import DataType
from typing import Any

DEFAULT_TRUE_VALUES: Any
DEFAULT_FALSE_VALUES: Any

class Boolean(DataType):
    true_values: Any = ...
    false_values: Any = ...
    def __init__(self, true_values: Any = ..., false_values: Any = ..., null_values: Any = ...) -> None: ...
    def cast(self, d: Any): ...
    def jsonify(self, d: Any): ...