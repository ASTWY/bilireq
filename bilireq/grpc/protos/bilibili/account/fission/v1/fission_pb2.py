# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/account/fission/v1/fission.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)bilibili/account/fission/v1/fission.proto\x12\x1b\x62ilibili.account.fission.v1\"\r\n\x0b\x45ntranceReq\"x\n\rEntranceReply\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12>\n\x0c\x61nimate_icon\x18\x04 \x01(\x0b\x32(.bilibili.account.fission.v1.AnimateIcon\"\x0b\n\tWindowReq\"=\n\x0bWindowReply\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x13\n\x0breport_data\x18\x03 \x01(\t\")\n\x0b\x41nimateIcon\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\x0c\n\x04json\x18\x02 \x01(\t2\xc7\x01\n\x07\x46ission\x12`\n\x08\x45ntrance\x12(.bilibili.account.fission.v1.EntranceReq\x1a*.bilibili.account.fission.v1.EntranceReply\x12Z\n\x06Window\x12&.bilibili.account.fission.v1.WindowReq\x1a(.bilibili.account.fission.v1.WindowReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.account.fission.v1.fission_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENTRANCEREQ._serialized_start=74
  _ENTRANCEREQ._serialized_end=87
  _ENTRANCEREPLY._serialized_start=89
  _ENTRANCEREPLY._serialized_end=209
  _WINDOWREQ._serialized_start=211
  _WINDOWREQ._serialized_end=222
  _WINDOWREPLY._serialized_start=224
  _WINDOWREPLY._serialized_end=285
  _ANIMATEICON._serialized_start=287
  _ANIMATEICON._serialized_end=328
  _FISSION._serialized_start=331
  _FISSION._serialized_end=530
# @@protoc_insertion_point(module_scope)
