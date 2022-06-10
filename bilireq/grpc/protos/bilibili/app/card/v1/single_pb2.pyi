"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilibili.app.card.v1.common_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class SmallCoverV5(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    COVER_GIF_FIELD_NUMBER: builtins.int
    UP_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_1_FIELD_NUMBER: builtins.int
    RIGHT_DESC_1_FIELD_NUMBER: builtins.int
    RIGHT_DESC_2_FIELD_NUMBER: builtins.int
    RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    HOTWORD_ENTRANCE_FIELD_NUMBER: builtins.int
    CORNER_MARK_STYLE_FIELD_NUMBER: builtins.int
    RIGHT_ICON_1_FIELD_NUMBER: builtins.int
    RIGHT_ICON_2_FIELD_NUMBER: builtins.int
    LEFT_CORNER_MARK_STYLE_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    cover_gif: typing.Text
    """"""

    @property
    def up(self) -> bilibili.app.card.v1.common_pb2.Up:
        """"""
        pass
    cover_right_text_1: typing.Text
    """封面右下角标文案"""

    right_desc_1: typing.Text
    """右侧文案1"""

    right_desc_2: typing.Text
    """右侧文案2"""

    @property
    def rcmd_reason_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """右侧推荐原因标签框"""
        pass
    @property
    def hotword_entrance(self) -> global___HotwordEntrance:
        """"""
        pass
    @property
    def corner_mark_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """直播小卡的角标"""
        pass
    right_icon_1: builtins.int
    """右侧文案1图标id"""

    right_icon_2: builtins.int
    """右侧文案2图标id"""

    @property
    def left_corner_mark_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """左上角角标"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        cover_gif: typing.Text = ...,
        up: typing.Optional[bilibili.app.card.v1.common_pb2.Up] = ...,
        cover_right_text_1: typing.Text = ...,
        right_desc_1: typing.Text = ...,
        right_desc_2: typing.Text = ...,
        rcmd_reason_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        hotword_entrance: typing.Optional[global___HotwordEntrance] = ...,
        corner_mark_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        right_icon_1: builtins.int = ...,
        right_icon_2: builtins.int = ...,
        left_corner_mark_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base","corner_mark_style",b"corner_mark_style","hotword_entrance",b"hotword_entrance","left_corner_mark_style",b"left_corner_mark_style","rcmd_reason_style",b"rcmd_reason_style","up",b"up"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","corner_mark_style",b"corner_mark_style","cover_gif",b"cover_gif","cover_right_text_1",b"cover_right_text_1","hotword_entrance",b"hotword_entrance","left_corner_mark_style",b"left_corner_mark_style","rcmd_reason_style",b"rcmd_reason_style","right_desc_1",b"right_desc_1","right_desc_2",b"right_desc_2","right_icon_1",b"right_icon_1","right_icon_2",b"right_icon_2","up",b"up"]) -> None: ...
global___SmallCoverV5 = SmallCoverV5

class HotwordEntrance(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HOTWORD_ID_FIELD_NUMBER: builtins.int
    HOT_TEXT_FIELD_NUMBER: builtins.int
    H5_URL_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    hotword_id: builtins.int
    """"""

    hot_text: typing.Text
    """"""

    h5_url: typing.Text
    """"""

    icon: typing.Text
    """"""

    def __init__(self,
        *,
        hotword_id: builtins.int = ...,
        hot_text: typing.Text = ...,
        h5_url: typing.Text = ...,
        icon: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["h5_url",b"h5_url","hot_text",b"hot_text","hotword_id",b"hotword_id","icon",b"icon"]) -> None: ...
global___HotwordEntrance = HotwordEntrance

class LargeCoverV1(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    COVER_GIF_FIELD_NUMBER: builtins.int
    AVATAR_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_1_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_2_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_3_FIELD_NUMBER: builtins.int
    COVER_BADGE_FIELD_NUMBER: builtins.int
    TOP_RCMD_REASON_FIELD_NUMBER: builtins.int
    BOTTOM_RCMD_REASON_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    OFFICIAL_ICON_FIELD_NUMBER: builtins.int
    CAN_PLAY_FIELD_NUMBER: builtins.int
    TOP_RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    BOTTOM_RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    RCMD_REASON_STYLE_V2_FIELD_NUMBER: builtins.int
    LEFT_COVER_BADGE_STYLE_FIELD_NUMBER: builtins.int
    RIGHT_COVER_BADGE_STYLE_FIELD_NUMBER: builtins.int
    COVER_BADGE_2_FIELD_NUMBER: builtins.int
    LIKE_BUTTON_FIELD_NUMBER: builtins.int
    TITLE_SINGLE_LINE_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    cover_gif: typing.Text
    """"""

    @property
    def avatar(self) -> bilibili.app.card.v1.common_pb2.Avatar:
        """"""
        pass
    cover_left_text_1: typing.Text
    """"""

    cover_left_text_2: typing.Text
    """"""

    cover_left_text_3: typing.Text
    """"""

    cover_badge: typing.Text
    """"""

    top_rcmd_reason: typing.Text
    """"""

    bottom_rcmd_reason: typing.Text
    """"""

    desc: typing.Text
    """"""

    official_icon: builtins.int
    """"""

    can_play: builtins.int
    """"""

    @property
    def top_rcmd_reason_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
        pass
    @property
    def bottom_rcmd_reason_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
        pass
    @property
    def rcmd_reason_style_v2(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
        pass
    @property
    def left_cover_badge_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
        pass
    @property
    def right_cover_badge_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
        pass
    cover_badge_2: typing.Text
    """"""

    @property
    def like_button(self) -> bilibili.app.card.v1.common_pb2.LikeButton:
        """"""
        pass
    title_single_line: builtins.int
    """"""

    cover_right_text: typing.Text
    """"""

    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        cover_gif: typing.Text = ...,
        avatar: typing.Optional[bilibili.app.card.v1.common_pb2.Avatar] = ...,
        cover_left_text_1: typing.Text = ...,
        cover_left_text_2: typing.Text = ...,
        cover_left_text_3: typing.Text = ...,
        cover_badge: typing.Text = ...,
        top_rcmd_reason: typing.Text = ...,
        bottom_rcmd_reason: typing.Text = ...,
        desc: typing.Text = ...,
        official_icon: builtins.int = ...,
        can_play: builtins.int = ...,
        top_rcmd_reason_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        bottom_rcmd_reason_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        rcmd_reason_style_v2: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        left_cover_badge_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        right_cover_badge_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        cover_badge_2: typing.Text = ...,
        like_button: typing.Optional[bilibili.app.card.v1.common_pb2.LikeButton] = ...,
        title_single_line: builtins.int = ...,
        cover_right_text: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["avatar",b"avatar","base",b"base","bottom_rcmd_reason_style",b"bottom_rcmd_reason_style","left_cover_badge_style",b"left_cover_badge_style","like_button",b"like_button","rcmd_reason_style_v2",b"rcmd_reason_style_v2","right_cover_badge_style",b"right_cover_badge_style","top_rcmd_reason_style",b"top_rcmd_reason_style"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["avatar",b"avatar","base",b"base","bottom_rcmd_reason",b"bottom_rcmd_reason","bottom_rcmd_reason_style",b"bottom_rcmd_reason_style","can_play",b"can_play","cover_badge",b"cover_badge","cover_badge_2",b"cover_badge_2","cover_gif",b"cover_gif","cover_left_text_1",b"cover_left_text_1","cover_left_text_2",b"cover_left_text_2","cover_left_text_3",b"cover_left_text_3","cover_right_text",b"cover_right_text","desc",b"desc","left_cover_badge_style",b"left_cover_badge_style","like_button",b"like_button","official_icon",b"official_icon","rcmd_reason_style_v2",b"rcmd_reason_style_v2","right_cover_badge_style",b"right_cover_badge_style","title_single_line",b"title_single_line","top_rcmd_reason",b"top_rcmd_reason","top_rcmd_reason_style",b"top_rcmd_reason_style"]) -> None: ...
global___LargeCoverV1 = LargeCoverV1

class ThreeItemAllV2(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    TOP_RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    ITEM_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    @property
    def top_rcmd_reason_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
        pass
    @property
    def item(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TwoItemHV1Item]:
        """"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        top_rcmd_reason_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        item: typing.Optional[typing.Iterable[global___TwoItemHV1Item]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base","top_rcmd_reason_style",b"top_rcmd_reason_style"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","item",b"item","top_rcmd_reason_style",b"top_rcmd_reason_style"]) -> None: ...
global___ThreeItemAllV2 = ThreeItemAllV2

class TwoItemHV1Item(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TITLE_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_1_FIELD_NUMBER: builtins.int
    COVER_LEFT_ICON_1_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_FIELD_NUMBER: builtins.int
    title: typing.Text
    """"""

    cover: typing.Text
    """"""

    uri: typing.Text
    """"""

    param: typing.Text
    """"""

    @property
    def args(self) -> bilibili.app.card.v1.common_pb2.Args:
        """"""
        pass
    goto: typing.Text
    """"""

    cover_left_text_1: typing.Text
    """"""

    cover_left_icon_1: builtins.int
    """"""

    cover_right_text: typing.Text
    """"""

    def __init__(self,
        *,
        title: typing.Text = ...,
        cover: typing.Text = ...,
        uri: typing.Text = ...,
        param: typing.Text = ...,
        args: typing.Optional[bilibili.app.card.v1.common_pb2.Args] = ...,
        goto: typing.Text = ...,
        cover_left_text_1: typing.Text = ...,
        cover_left_icon_1: builtins.int = ...,
        cover_right_text: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args",b"args"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","cover",b"cover","cover_left_icon_1",b"cover_left_icon_1","cover_left_text_1",b"cover_left_text_1","cover_right_text",b"cover_right_text","goto",b"goto","param",b"param","title",b"title","uri",b"uri"]) -> None: ...
global___TwoItemHV1Item = TwoItemHV1Item

class RcmdOneItem(google.protobuf.message.Message):
    """推荐"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    TOPRCMDREASONSTYLE_FIELD_NUMBER: builtins.int
    ITEM_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    @property
    def topRcmdReasonStyle(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """标签框信息"""
        pass
    @property
    def item(self) -> global___SmallCoverRcmdItem:
        """小封面推荐内容信息"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        topRcmdReasonStyle: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        item: typing.Optional[global___SmallCoverRcmdItem] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base","item",b"item","topRcmdReasonStyle",b"topRcmdReasonStyle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","item",b"item","topRcmdReasonStyle",b"topRcmdReasonStyle"]) -> None: ...
global___RcmdOneItem = RcmdOneItem

class SmallCoverRcmdItem(google.protobuf.message.Message):
    """小封面推荐内容信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TITLE_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    COVERRIGHTTEXT1_FIELD_NUMBER: builtins.int
    RIGHTDESC1_FIELD_NUMBER: builtins.int
    RIGHTDESC2_FIELD_NUMBER: builtins.int
    COVERGIF_FIELD_NUMBER: builtins.int
    RIGHTICON1_FIELD_NUMBER: builtins.int
    RIGHTICON2_FIELD_NUMBER: builtins.int
    title: typing.Text
    """标题"""

    cover: typing.Text
    """封面url"""

    uri: typing.Text
    """跳转uri"""

    param: typing.Text
    """参数"""

    goto: typing.Text
    """跳转类型
    av:视频稿件
    """

    coverRightText1: typing.Text
    """封面右下角标文案"""

    rightDesc1: typing.Text
    """右侧文案1"""

    rightDesc2: typing.Text
    """右侧文案2"""

    coverGif: typing.Text
    """"""

    rightIcon1: builtins.int
    """右侧文案1图标id"""

    rightIcon2: builtins.int
    """右侧文案2图标id"""

    def __init__(self,
        *,
        title: typing.Text = ...,
        cover: typing.Text = ...,
        uri: typing.Text = ...,
        param: typing.Text = ...,
        goto: typing.Text = ...,
        coverRightText1: typing.Text = ...,
        rightDesc1: typing.Text = ...,
        rightDesc2: typing.Text = ...,
        coverGif: typing.Text = ...,
        rightIcon1: builtins.int = ...,
        rightIcon2: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cover",b"cover","coverGif",b"coverGif","coverRightText1",b"coverRightText1","goto",b"goto","param",b"param","rightDesc1",b"rightDesc1","rightDesc2",b"rightDesc2","rightIcon1",b"rightIcon1","rightIcon2",b"rightIcon2","title",b"title","uri",b"uri"]) -> None: ...
global___SmallCoverRcmdItem = SmallCoverRcmdItem

class ThreeItemV1(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    TITLEICON_FIELD_NUMBER: builtins.int
    MOREURI_FIELD_NUMBER: builtins.int
    MORETEXT_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    titleIcon: builtins.int
    """"""

    moreUri: typing.Text
    """"""

    moreText: typing.Text
    """"""

    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThreeItemV1Item]:
        """"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        titleIcon: builtins.int = ...,
        moreUri: typing.Text = ...,
        moreText: typing.Text = ...,
        items: typing.Optional[typing.Iterable[global___ThreeItemV1Item]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","items",b"items","moreText",b"moreText","moreUri",b"moreUri","titleIcon",b"titleIcon"]) -> None: ...
global___ThreeItemV1 = ThreeItemV1

class ThreeItemV1Item(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    COVERLEFTTEXT_FIELD_NUMBER: builtins.int
    COVERLEFTICON_FIELD_NUMBER: builtins.int
    DESC1_FIELD_NUMBER: builtins.int
    DESC2_FIELD_NUMBER: builtins.int
    BADGE_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    coverLeftText: typing.Text
    """"""

    coverLeftIcon: builtins.int
    """"""

    desc1: typing.Text
    """"""

    desc2: typing.Text
    """"""

    badge: typing.Text
    """"""

    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        coverLeftText: typing.Text = ...,
        coverLeftIcon: builtins.int = ...,
        desc1: typing.Text = ...,
        desc2: typing.Text = ...,
        badge: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["badge",b"badge","base",b"base","coverLeftIcon",b"coverLeftIcon","coverLeftText",b"coverLeftText","desc1",b"desc1","desc2",b"desc2"]) -> None: ...
global___ThreeItemV1Item = ThreeItemV1Item

class HotTopicItem(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COVER_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    cover: typing.Text
    """"""

    uri: typing.Text
    """"""

    param: typing.Text
    """"""

    name: typing.Text
    """"""

    def __init__(self,
        *,
        cover: typing.Text = ...,
        uri: typing.Text = ...,
        param: typing.Text = ...,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cover",b"cover","name",b"name","param",b"param","uri",b"uri"]) -> None: ...
global___HotTopicItem = HotTopicItem

class HotTopic(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    desc: typing.Text
    """"""

    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HotTopicItem]:
        """"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        desc: typing.Text = ...,
        items: typing.Optional[typing.Iterable[global___HotTopicItem]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","desc",b"desc","items",b"items"]) -> None: ...
global___HotTopic = HotTopic

class DynamicHot(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    TOP_LEFT_TITLE_FIELD_NUMBER: builtins.int
    DESC1_FIELD_NUMBER: builtins.int
    DESC2_FIELD_NUMBER: builtins.int
    MORE_URI_FIELD_NUMBER: builtins.int
    MORE_TEXT_FIELD_NUMBER: builtins.int
    COVERS_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_FIELD_NUMBER: builtins.int
    TOP_RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    top_left_title: typing.Text
    """"""

    desc1: typing.Text
    """"""

    desc2: typing.Text
    """"""

    more_uri: typing.Text
    """"""

    more_text: typing.Text
    """"""

    @property
    def covers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """"""
        pass
    cover_right_text: typing.Text
    """"""

    @property
    def top_rcmd_reason_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        top_left_title: typing.Text = ...,
        desc1: typing.Text = ...,
        desc2: typing.Text = ...,
        more_uri: typing.Text = ...,
        more_text: typing.Text = ...,
        covers: typing.Optional[typing.Iterable[typing.Text]] = ...,
        cover_right_text: typing.Text = ...,
        top_rcmd_reason_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base","top_rcmd_reason_style",b"top_rcmd_reason_style"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","cover_right_text",b"cover_right_text","covers",b"covers","desc1",b"desc1","desc2",b"desc2","more_text",b"more_text","more_uri",b"more_uri","top_left_title",b"top_left_title","top_rcmd_reason_style",b"top_rcmd_reason_style"]) -> None: ...
global___DynamicHot = DynamicHot

class MiddleCoverV3(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    DESC1_FIELD_NUMBER: builtins.int
    DESC2_FIELD_NUMBER: builtins.int
    COVER_BADGE_STYLE_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    desc1: typing.Text
    """"""

    desc2: typing.Text
    """"""

    @property
    def cover_badge_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        desc1: typing.Text = ...,
        desc2: typing.Text = ...,
        cover_badge_style: typing.Optional[bilibili.app.card.v1.common_pb2.ReasonStyle] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base","cover_badge_style",b"cover_badge_style"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","cover_badge_style",b"cover_badge_style","desc1",b"desc1","desc2",b"desc2"]) -> None: ...
global___MiddleCoverV3 = MiddleCoverV3

class LargeCoverV4(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_1_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_2_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_3_FIELD_NUMBER: builtins.int
    COVER_BADGE_FIELD_NUMBER: builtins.int
    CAN_PLAY_FIELD_NUMBER: builtins.int
    UP_FIELD_NUMBER: builtins.int
    SHORT_LINK_FIELD_NUMBER: builtins.int
    SHARE_SUBTITLE_FIELD_NUMBER: builtins.int
    PLAY_NUMBER_FIELD_NUMBER: builtins.int
    BVID_FIELD_NUMBER: builtins.int
    SUB_PARAM_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    cover_left_text_1: typing.Text
    """"""

    cover_left_text_2: typing.Text
    """"""

    cover_left_text_3: typing.Text
    """"""

    cover_badge: typing.Text
    """"""

    can_play: builtins.int
    """"""

    @property
    def up(self) -> bilibili.app.card.v1.common_pb2.Up:
        """"""
        pass
    short_link: typing.Text
    """"""

    share_subtitle: typing.Text
    """"""

    play_number: typing.Text
    """"""

    bvid: typing.Text
    """"""

    sub_param: typing.Text
    """"""

    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        cover_left_text_1: typing.Text = ...,
        cover_left_text_2: typing.Text = ...,
        cover_left_text_3: typing.Text = ...,
        cover_badge: typing.Text = ...,
        can_play: builtins.int = ...,
        up: typing.Optional[bilibili.app.card.v1.common_pb2.Up] = ...,
        short_link: typing.Text = ...,
        share_subtitle: typing.Text = ...,
        play_number: typing.Text = ...,
        bvid: typing.Text = ...,
        sub_param: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base","up",b"up"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","bvid",b"bvid","can_play",b"can_play","cover_badge",b"cover_badge","cover_left_text_1",b"cover_left_text_1","cover_left_text_2",b"cover_left_text_2","cover_left_text_3",b"cover_left_text_3","play_number",b"play_number","share_subtitle",b"share_subtitle","short_link",b"short_link","sub_param",b"sub_param","up",b"up"]) -> None: ...
global___LargeCoverV4 = LargeCoverV4

class PopularTopEntrance(google.protobuf.message.Message):
    """热门列表顶部按钮"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
        pass
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntranceItem]:
        """按钮项"""
        pass
    def __init__(self,
        *,
        base: typing.Optional[bilibili.app.card.v1.common_pb2.Base] = ...,
        items: typing.Optional[typing.Iterable[global___EntranceItem]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base",b"base"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base",b"base","items",b"items"]) -> None: ...
global___PopularTopEntrance = PopularTopEntrance

class EntranceItem(google.protobuf.message.Message):
    """热门列表按钮信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GOTO_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    MODULE_ID_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    ENTRANCE_ID_FIELD_NUMBER: builtins.int
    BUBBLE_FIELD_NUMBER: builtins.int
    ENTRANCE_TYPE_FIELD_NUMBER: builtins.int
    goto: typing.Text
    """跳转类型"""

    icon: typing.Text
    """图标url"""

    title: typing.Text
    """标题"""

    module_id: typing.Text
    """入口模块id"""

    uri: typing.Text
    """跳转uri"""

    entrance_id: builtins.int
    """入口id"""

    @property
    def bubble(self) -> global___Bubble:
        """气泡信息"""
        pass
    entrance_type: builtins.int
    """入口类型
    1:代表分品类热门
    """

    def __init__(self,
        *,
        goto: typing.Text = ...,
        icon: typing.Text = ...,
        title: typing.Text = ...,
        module_id: typing.Text = ...,
        uri: typing.Text = ...,
        entrance_id: builtins.int = ...,
        bubble: typing.Optional[global___Bubble] = ...,
        entrance_type: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bubble",b"bubble"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bubble",b"bubble","entrance_id",b"entrance_id","entrance_type",b"entrance_type","goto",b"goto","icon",b"icon","module_id",b"module_id","title",b"title","uri",b"uri"]) -> None: ...
global___EntranceItem = EntranceItem

class Bubble(google.protobuf.message.Message):
    """气泡信息"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BUBBLE_CONTENT_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    STIME_FIELD_NUMBER: builtins.int
    bubble_content: typing.Text
    """文案"""

    version: builtins.int
    """版本"""

    stime: builtins.int
    """起始时间"""

    def __init__(self,
        *,
        bubble_content: typing.Text = ...,
        version: builtins.int = ...,
        stime: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bubble_content",b"bubble_content","stime",b"stime","version",b"version"]) -> None: ...
global___Bubble = Bubble