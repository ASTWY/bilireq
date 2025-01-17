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

class DanmukuEvent(google.protobuf.message.Message):
    """实时弹幕事件"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ELEMS_FIELD_NUMBER: builtins.int
    @property
    def elems(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DanmakuElem]:
        """弹幕列表"""
    def __init__(
        self,
        *,
        elems: collections.abc.Iterable[global___DanmakuElem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["elems", b"elems"]) -> None: ...

global___DanmukuEvent = DanmukuEvent

class DanmakuElem(google.protobuf.message.Message):
    """弹幕条目"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    FONTSIZE_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    MID_HASH_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    CTIME_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    POOL_FIELD_NUMBER: builtins.int
    ID_STR_FIELD_NUMBER: builtins.int
    id: builtins.int
    """弹幕dmid"""
    progress: builtins.int
    """弹幕出现位置(单位为ms)"""
    mode: builtins.int
    """弹幕类型"""
    fontsize: builtins.int
    """弹幕字号"""
    color: builtins.int
    """弹幕颜色"""
    mid_hash: builtins.str
    """发送着mid hash"""
    content: builtins.str
    """弹幕正文"""
    ctime: builtins.int
    """发送时间"""
    action: builtins.str
    """弹幕动作"""
    pool: builtins.int
    """弹幕池"""
    id_str: builtins.str
    """弹幕id str"""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        progress: builtins.int = ...,
        mode: builtins.int = ...,
        fontsize: builtins.int = ...,
        color: builtins.int = ...,
        mid_hash: builtins.str = ...,
        content: builtins.str = ...,
        ctime: builtins.int = ...,
        action: builtins.str = ...,
        pool: builtins.int = ...,
        id_str: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "color", b"color", "content", b"content", "ctime", b"ctime", "fontsize", b"fontsize", "id", b"id", "id_str", b"id_str", "mid_hash", b"mid_hash", "mode", b"mode", "pool", b"pool", "progress", b"progress"]) -> None: ...

global___DanmakuElem = DanmakuElem

class CommandDm(google.protobuf.message.Message):
    """互动弹幕"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    OID_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    CTIME_FIELD_NUMBER: builtins.int
    MTIME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    IDSTR_FIELD_NUMBER: builtins.int
    id: builtins.int
    """弹幕id"""
    oid: builtins.int
    """对象视频cid"""
    mid: builtins.int
    """发送者mid"""
    type: builtins.int
    """"""
    command: builtins.str
    """互动弹幕指令"""
    content: builtins.str
    """互动弹幕正文"""
    state: builtins.int
    """弹幕状态"""
    progress: builtins.int
    """出现时间"""
    ctime: builtins.str
    """创建时间"""
    mtime: builtins.str
    """发布时间"""
    extra: builtins.str
    """扩展json数据"""
    idStr: builtins.str
    """弹幕id str类型"""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        oid: builtins.int = ...,
        mid: builtins.int = ...,
        type: builtins.int = ...,
        command: builtins.str = ...,
        content: builtins.str = ...,
        state: builtins.int = ...,
        progress: builtins.int = ...,
        ctime: builtins.str = ...,
        mtime: builtins.str = ...,
        extra: builtins.str = ...,
        idStr: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["command", b"command", "content", b"content", "ctime", b"ctime", "extra", b"extra", "id", b"id", "idStr", b"idStr", "mid", b"mid", "mtime", b"mtime", "oid", b"oid", "progress", b"progress", "state", b"state", "type", b"type"]) -> None: ...

global___CommandDm = CommandDm
