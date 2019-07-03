# Stubs for agate.data_types.date (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from agate.data_types.base import DataType
from typing import Any, Optional

ZERO_DT: Any

class Date(DataType):
    date_format: Any = ...
    parser: Any = ...
    def __init__(self, date_format: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def cast(self, d: Any): ...
    def csvify(self, d: Any): ...
    def jsonify(self, d: Any): ...