"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AddParams(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    A_FIELD_NUMBER: builtins.int
    B_FIELD_NUMBER: builtins.int
    a: builtins.int
    """"""
    b: builtins.int
    """"""
    def __init__(
        self,
        *,
        a: builtins.int = ...,
        b: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["a", b"a", "b", b"b"]) -> None: ...

global___AddParams = AddParams

class AddResult(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    R_FIELD_NUMBER: builtins.int
    r: builtins.int
    """"""
    def __init__(
        self,
        *,
        r: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["r", b"r"]) -> None: ...

global___AddResult = AddResult

class TestResp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASKID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    taskid: builtins.int
    """任务id"""
    timestamp: builtins.int
    """时间戳"""
    message: builtins.str
    """消息"""
    @property
    def extra(self) -> google.protobuf.any_pb2.Any:
        """扩展"""
    def __init__(
        self,
        *,
        taskid: builtins.int = ...,
        timestamp: builtins.int = ...,
        message: builtins.str = ...,
        extra: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["extra", b"extra"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["extra", b"extra", "message", b"message", "taskid", b"taskid", "timestamp", b"timestamp"]) -> None: ...

global___TestResp = TestResp
