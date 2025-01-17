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

class PremiereStatusReq(google.protobuf.message.Message):
    """获取首播状态-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EP_ID_FIELD_NUMBER: builtins.int
    ep_id: builtins.int
    """剧集epid"""
    def __init__(
        self,
        *,
        ep_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ep_id", b"ep_id"]) -> None: ...

global___PremiereStatusReq = PremiereStatusReq

class PremiereStatusReply(google.protobuf.message.Message):
    """获取首播状态-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROGRESS_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    DELAY_TIME_FIELD_NUMBER: builtins.int
    ONLINE_COUNT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    AFTER_PREMIERE_TYPE_FIELD_NUMBER: builtins.int
    progress: builtins.int
    """服务端播放进度 单位ms 用户实际播放进度：progress - delay_time"""
    start_time: builtins.int
    """起播时间戳 单位ms"""
    delay_time: builtins.int
    """延迟播放时长 单位ms"""
    online_count: builtins.int
    """首播在线人数"""
    status: builtins.int
    """首播状态
    1:预热 2:首播中 3:紧急停播 4:已结束
    """
    after_premiere_type: builtins.int
    """首播结束后跳转类型
    1:下架 2:转点播
    """
    def __init__(
        self,
        *,
        progress: builtins.int = ...,
        start_time: builtins.int = ...,
        delay_time: builtins.int = ...,
        online_count: builtins.int = ...,
        status: builtins.int = ...,
        after_premiere_type: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["after_premiere_type", b"after_premiere_type", "delay_time", b"delay_time", "online_count", b"online_count", "progress", b"progress", "start_time", b"start_time", "status", b"status"]) -> None: ...

global___PremiereStatusReply = PremiereStatusReply
