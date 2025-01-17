"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MessagePullsReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    PN_FIELD_NUMBER: builtins.int
    PS_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    HAS_NEXT_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """"""
    pn: builtins.int
    """"""
    ps: builtins.int
    """"""
    count: builtins.int
    """"""
    has_next: builtins.bool
    """"""
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        pn: builtins.int = ...,
        ps: builtins.int = ...,
        count: builtins.int = ...,
        has_next: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["count", b"count", "data", b"data", "has_next", b"has_next", "pn", b"pn", "ps", b"ps"]) -> None: ...

global___MessagePullsReply = MessagePullsReply

class MessagePullsReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_SEQ_ID_FIELD_NUMBER: builtins.int
    END_SEQ_ID_FIELD_NUMBER: builtins.int
    PN_FIELD_NUMBER: builtins.int
    PS_FIELD_NUMBER: builtins.int
    start_seq_id: builtins.int
    """"""
    end_seq_id: builtins.int
    """"""
    pn: builtins.int
    """"""
    ps: builtins.int
    """"""
    def __init__(
        self,
        *,
        start_seq_id: builtins.int = ...,
        end_seq_id: builtins.int = ...,
        pn: builtins.int = ...,
        ps: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_seq_id", b"end_seq_id", "pn", b"pn", "ps", b"ps", "start_seq_id", b"start_seq_id"]) -> None: ...

global___MessagePullsReq = MessagePullsReq
