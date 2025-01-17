"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Exp(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    BUCKET_FIELD_NUMBER: builtins.int
    id: builtins.int
    """"""
    bucket: builtins.int
    """"""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        bucket: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bucket", b"bucket", "id", b"id"]) -> None: ...

global___Exp = Exp

class Exps(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXPS_FIELD_NUMBER: builtins.int
    @property
    def exps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Exp]:
        """"""
    def __init__(
        self,
        *,
        exps: collections.abc.Iterable[global___Exp] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exps", b"exps"]) -> None: ...

global___Exps = Exps
