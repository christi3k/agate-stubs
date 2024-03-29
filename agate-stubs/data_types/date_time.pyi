# Stubs for agate.data_types.date_time (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from agate.data_types.base import DataType
from typing import Any, Optional

class DateTime(DataType):
    datetime_format: Any = ...
    timezone: Any = ...
    def __init__(self, datetime_format: Optional[Any] = ..., timezone: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def cast(self, d: Any): ...
    def csvify(self, d: Any): ...
    def jsonify(self, d: Any): ...
