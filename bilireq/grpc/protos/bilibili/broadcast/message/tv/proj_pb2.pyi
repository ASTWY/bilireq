"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ProjReply(google.protobuf.message.Message):
    """投屏"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CMD_TYPE_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    AID_FIELD_NUMBER: builtins.int
    CID_FIELD_NUMBER: builtins.int
    VIDEO_TYPE_FIELD_NUMBER: builtins.int
    EP_ID_FIELD_NUMBER: builtins.int
    SEASON_ID_FIELD_NUMBER: builtins.int
    SEEK_TS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    cmd_type: builtins.int
    """投屏命令
    1:起播 2:快进 3:快退 4:seek播放进度 5:暂停 6:暂停恢复
    """
    mid: builtins.int
    """用户id"""
    aid: builtins.int
    """稿件id"""
    cid: builtins.int
    """视频id"""
    video_type: builtins.int
    """视频类型
    0:ugc 1:pgc 2:pugv
    """
    ep_id: builtins.int
    """单集id，pgc和pugv需要传"""
    season_id: builtins.int
    """剧集id"""
    seek_ts: builtins.int
    """seek 的位置，cmd位seek时有值，单位秒"""
    extra: builtins.str
    """其他指令对应内容"""
    def __init__(
        self,
        *,
        cmd_type: builtins.int = ...,
        mid: builtins.int = ...,
        aid: builtins.int = ...,
        cid: builtins.int = ...,
        video_type: builtins.int = ...,
        ep_id: builtins.int = ...,
        season_id: builtins.int = ...,
        seek_ts: builtins.int = ...,
        extra: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aid", b"aid", "cid", b"cid", "cmd_type", b"cmd_type", "ep_id", b"ep_id", "extra", b"extra", "mid", b"mid", "season_id", b"season_id", "seek_ts", b"seek_ts", "video_type", b"video_type"]) -> None: ...

global___ProjReply = ProjReply

class LiveStatusNotify(google.protobuf.message.Message):
    """直播状态"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    CID_FIELD_NUMBER: builtins.int
    status: builtins.int
    """直播状态
    1:开播 2:关播 3:截流 4:截流恢复
    """
    msg: builtins.str
    """文案"""
    cid: builtins.int
    """直播房间号"""
    def __init__(
        self,
        *,
        status: builtins.int = ...,
        msg: builtins.str = ...,
        cid: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cid", b"cid", "msg", b"msg", "status", b"status"]) -> None: ...

global___LiveStatusNotify = LiveStatusNotify

class EsportsNotify(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CID_FIELD_NUMBER: builtins.int
    cid: builtins.int
    """直播房间号"""
    def __init__(
        self,
        *,
        cid: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cid", b"cid"]) -> None: ...

global___EsportsNotify = EsportsNotify

class PublicityNotify(google.protobuf.message.Message):
    """直播插卡"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUBLICITY_ID_FIELD_NUMBER: builtins.int
    ROOM_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    publicity_id: builtins.int
    """插卡id"""
    room_id: builtins.int
    """直播房间号"""
    status: builtins.int
    """直播间状态
    0:未开播 1:直播中 2:轮播中
    """
    def __init__(
        self,
        *,
        publicity_id: builtins.int = ...,
        room_id: builtins.int = ...,
        status: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["publicity_id", b"publicity_id", "room_id", b"room_id", "status", b"status"]) -> None: ...

global___PublicityNotify = PublicityNotify

class LiveSkipNotify(google.protobuf.message.Message):
    """直转点"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIVE_ID_FIELD_NUMBER: builtins.int
    live_id: builtins.int
    """直播id"""
    def __init__(
        self,
        *,
        live_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["live_id", b"live_id"]) -> None: ...

global___LiveSkipNotify = LiveSkipNotify
