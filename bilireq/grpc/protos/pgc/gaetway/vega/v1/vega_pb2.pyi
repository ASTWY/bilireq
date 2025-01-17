"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.rpc.status_pb2
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

class AuthReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AuthReq = AuthReq

class AuthResp(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AuthResp = AuthResp

class FrameOption(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VEGA_ID_FIELD_NUMBER: builtins.int
    REQ_ID_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    IS_ACK_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ACK_ORIGIN_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    vega_id: builtins.int
    """"""
    req_id: builtins.str
    """"""
    sequence: builtins.int
    """"""
    is_ack: builtins.bool
    """"""
    @property
    def status(self) -> bilibili.rpc.status_pb2.Status:
        """"""
    ack_origin: builtins.str
    """"""
    mid: builtins.int
    """"""
    def __init__(
        self,
        *,
        vega_id: builtins.int = ...,
        req_id: builtins.str = ...,
        sequence: builtins.int = ...,
        is_ack: builtins.bool = ...,
        status: bilibili.rpc.status_pb2.Status | None = ...,
        ack_origin: builtins.str = ...,
        mid: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ack_origin", b"ack_origin", "is_ack", b"is_ack", "mid", b"mid", "req_id", b"req_id", "sequence", b"sequence", "status", b"status", "vega_id", b"vega_id"]) -> None: ...

global___FrameOption = FrameOption

class HeartbeatReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___HeartbeatReq = HeartbeatReq

class HeartbeatResp(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___HeartbeatResp = HeartbeatResp

class MessageAckReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VEGA_ID_FIELD_NUMBER: builtins.int
    REQ_ID_FIELD_NUMBER: builtins.int
    ORIGIN_FIELD_NUMBER: builtins.int
    TARGET_PATH_FIELD_NUMBER: builtins.int
    vega_id: builtins.str
    """"""
    req_id: builtins.str
    """"""
    origin: builtins.str
    """"""
    target_path: builtins.str
    """"""
    def __init__(
        self,
        *,
        vega_id: builtins.str = ...,
        req_id: builtins.str = ...,
        origin: builtins.str = ...,
        target_path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["origin", b"origin", "req_id", b"req_id", "target_path", b"target_path", "vega_id", b"vega_id"]) -> None: ...

global___MessageAckReq = MessageAckReq

class SubscribeReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_PATHS_FIELD_NUMBER: builtins.int
    @property
    def target_paths(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TargetPath]:
        """"""
    def __init__(
        self,
        *,
        target_paths: collections.abc.Iterable[global___TargetPath] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["target_paths", b"target_paths"]) -> None: ...

global___SubscribeReq = SubscribeReq

class TargetPath(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    SUBS_FIELD_NUMBER: builtins.int
    key: builtins.str
    """"""
    @property
    def subs(self) -> google.protobuf.any_pb2.Any:
        """"""
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        subs: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["subs", b"subs"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "subs", b"subs"]) -> None: ...

global___TargetPath = TargetPath

class VegaFrame(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPTIONS_FIELD_NUMBER: builtins.int
    ROUTE_PATH_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    SUB_BIZ_FIELD_NUMBER: builtins.int
    @property
    def options(self) -> global___FrameOption:
        """"""
    route_path: builtins.str
    """"""
    @property
    def body(self) -> google.protobuf.any_pb2.Any:
        """"""
    @property
    def sub_biz(self) -> google.protobuf.any_pb2.Any:
        """"""
    def __init__(
        self,
        *,
        options: global___FrameOption | None = ...,
        route_path: builtins.str = ...,
        body: google.protobuf.any_pb2.Any | None = ...,
        sub_biz: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body", b"body", "options", b"options", "sub_biz", b"sub_biz"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body", b"body", "options", b"options", "route_path", b"route_path", "sub_biz", b"sub_biz"]) -> None: ...

global___VegaFrame = VegaFrame
