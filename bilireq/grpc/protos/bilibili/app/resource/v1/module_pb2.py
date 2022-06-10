# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/resource/v1/module.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bilibili/app/resource/v1/module.proto\x12\x18\x62ilibili.app.resource.v1\"b\n\tListReply\x12\x0b\n\x03\x65nv\x18\x01 \x01(\t\x12\x32\n\x05pools\x18\x02 \x03(\x0b\x32#.bilibili.app.resource.v1.PoolReply\x12\x14\n\x0clist_version\x18\x03 \x01(\x03\"\xe5\x01\n\x07ListReq\x12\x11\n\tpool_name\x18\x01 \x01(\t\x12\x13\n\x0bmodule_name\x18\x02 \x01(\t\x12>\n\x0cversion_list\x18\x03 \x03(\x0b\x32(.bilibili.app.resource.v1.VersionListReq\x12.\n\x03\x65nv\x18\x04 \x01(\x0e\x32!.bilibili.app.resource.v1.EnvType\x12\x0f\n\x07sys_ver\x18\x05 \x01(\x05\x12\r\n\x05scale\x18\x06 \x01(\x05\x12\x0c\n\x04\x61rch\x18\x07 \x01(\x05\x12\x14\n\x0clist_version\x18\x08 \x01(\x03\"\xbe\x03\n\x0bModuleReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0b\n\x03md5\x18\x04 \x01(\t\x12\x11\n\ttotal_md5\x18\x05 \x01(\t\x12:\n\tincrement\x18\x06 \x01(\x0e\x32\'.bilibili.app.resource.v1.IncrementType\x12\x0f\n\x07is_wifi\x18\x07 \x01(\x08\x12\x32\n\x05level\x18\x08 \x01(\x0e\x32#.bilibili.app.resource.v1.LevelType\x12\x10\n\x08\x66ilename\x18\t \x01(\t\x12\x11\n\tfile_type\x18\n \x01(\t\x12\x11\n\tfile_size\x18\x0b \x01(\x03\x12\x38\n\x08\x63ompress\x18\x0c \x01(\x0e\x32&.bilibili.app.resource.v1.CompressType\x12\x14\n\x0cpublish_time\x18\r \x01(\x03\x12\x0f\n\x07pool_id\x18\x0e \x01(\x03\x12\x11\n\tmodule_id\x18\x0f \x01(\x03\x12\x12\n\nversion_id\x18\x10 \x01(\x03\x12\x0f\n\x07\x66ile_id\x18\x11 \x01(\x03\x12\x11\n\tzip_check\x18\x12 \x01(\x08\"Q\n\tPoolReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x07modules\x18\x02 \x03(\x0b\x32%.bilibili.app.resource.v1.ModuleReply\"[\n\x0eVersionListReq\x12\x11\n\tpool_name\x18\x01 \x01(\t\x12\x36\n\x08versions\x18\x02 \x03(\x0b\x32$.bilibili.app.resource.v1.VersionReq\"2\n\nVersionReq\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03*\'\n\x0c\x43ompressType\x12\t\n\x05Unzip\x10\x00\x12\x0c\n\x08Original\x10\x01*-\n\x07\x45nvType\x12\x0b\n\x07Unknown\x10\x00\x12\x0b\n\x07Release\x10\x01\x12\x08\n\x04Test\x10\x02*+\n\rIncrementType\x12\t\n\x05Total\x10\x00\x12\x0f\n\x0bIncremental\x10\x01*9\n\tLevelType\x12\r\n\tUndefined\x10\x00\x12\x08\n\x04High\x10\x01\x12\n\n\x06Middle\x10\x02\x12\x07\n\x03Low\x10\x03\x32X\n\x06Module\x12N\n\x04List\x12!.bilibili.app.resource.v1.ListReq\x1a#.bilibili.app.resource.v1.ListReplyb\x06proto3')

_COMPRESSTYPE = DESCRIPTOR.enum_types_by_name['CompressType']
CompressType = enum_type_wrapper.EnumTypeWrapper(_COMPRESSTYPE)
_ENVTYPE = DESCRIPTOR.enum_types_by_name['EnvType']
EnvType = enum_type_wrapper.EnumTypeWrapper(_ENVTYPE)
_INCREMENTTYPE = DESCRIPTOR.enum_types_by_name['IncrementType']
IncrementType = enum_type_wrapper.EnumTypeWrapper(_INCREMENTTYPE)
_LEVELTYPE = DESCRIPTOR.enum_types_by_name['LevelType']
LevelType = enum_type_wrapper.EnumTypeWrapper(_LEVELTYPE)
Unzip = 0
Original = 1
Unknown = 0
Release = 1
Test = 2
Total = 0
Incremental = 1
Undefined = 0
High = 1
Middle = 2
Low = 3


_LISTREPLY = DESCRIPTOR.message_types_by_name['ListReply']
_LISTREQ = DESCRIPTOR.message_types_by_name['ListReq']
_MODULEREPLY = DESCRIPTOR.message_types_by_name['ModuleReply']
_POOLREPLY = DESCRIPTOR.message_types_by_name['PoolReply']
_VERSIONLISTREQ = DESCRIPTOR.message_types_by_name['VersionListReq']
_VERSIONREQ = DESCRIPTOR.message_types_by_name['VersionReq']
ListReply = _reflection.GeneratedProtocolMessageType('ListReply', (_message.Message,), {
  'DESCRIPTOR' : _LISTREPLY,
  '__module__' : 'bilibili.app.resource.v1.module_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.resource.v1.ListReply)
  })
_sym_db.RegisterMessage(ListReply)

ListReq = _reflection.GeneratedProtocolMessageType('ListReq', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQ,
  '__module__' : 'bilibili.app.resource.v1.module_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.resource.v1.ListReq)
  })
_sym_db.RegisterMessage(ListReq)

ModuleReply = _reflection.GeneratedProtocolMessageType('ModuleReply', (_message.Message,), {
  'DESCRIPTOR' : _MODULEREPLY,
  '__module__' : 'bilibili.app.resource.v1.module_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.resource.v1.ModuleReply)
  })
_sym_db.RegisterMessage(ModuleReply)

PoolReply = _reflection.GeneratedProtocolMessageType('PoolReply', (_message.Message,), {
  'DESCRIPTOR' : _POOLREPLY,
  '__module__' : 'bilibili.app.resource.v1.module_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.resource.v1.PoolReply)
  })
_sym_db.RegisterMessage(PoolReply)

VersionListReq = _reflection.GeneratedProtocolMessageType('VersionListReq', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONLISTREQ,
  '__module__' : 'bilibili.app.resource.v1.module_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.resource.v1.VersionListReq)
  })
_sym_db.RegisterMessage(VersionListReq)

VersionReq = _reflection.GeneratedProtocolMessageType('VersionReq', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONREQ,
  '__module__' : 'bilibili.app.resource.v1.module_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.resource.v1.VersionReq)
  })
_sym_db.RegisterMessage(VersionReq)

_MODULE = DESCRIPTOR.services_by_name['Module']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPRESSTYPE._serialized_start=1076
  _COMPRESSTYPE._serialized_end=1115
  _ENVTYPE._serialized_start=1117
  _ENVTYPE._serialized_end=1162
  _INCREMENTTYPE._serialized_start=1164
  _INCREMENTTYPE._serialized_end=1207
  _LEVELTYPE._serialized_start=1209
  _LEVELTYPE._serialized_end=1266
  _LISTREPLY._serialized_start=67
  _LISTREPLY._serialized_end=165
  _LISTREQ._serialized_start=168
  _LISTREQ._serialized_end=397
  _MODULEREPLY._serialized_start=400
  _MODULEREPLY._serialized_end=846
  _POOLREPLY._serialized_start=848
  _POOLREPLY._serialized_end=929
  _VERSIONLISTREQ._serialized_start=931
  _VERSIONLISTREQ._serialized_end=1022
  _VERSIONREQ._serialized_start=1024
  _VERSIONREQ._serialized_end=1074
  _MODULE._serialized_start=1268
  _MODULE._serialized_end=1356
# @@protoc_insertion_point(module_scope)