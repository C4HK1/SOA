# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: my_grpc.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'my_grpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmy_grpc.proto\x12\x06mygrpc\"\x19\n\tMyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nMyResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2>\n\tMyService\x12\x31\n\x08MyMethod\x12\x11.mygrpc.MyRequest\x1a\x12.mygrpc.MyResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_grpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MYREQUEST']._serialized_start=25
  _globals['_MYREQUEST']._serialized_end=50
  _globals['_MYRESPONSE']._serialized_start=52
  _globals['_MYRESPONSE']._serialized_end=81
  _globals['_MYSERVICE']._serialized_start=83
  _globals['_MYSERVICE']._serialized_end=145
# @@protoc_insertion_point(module_scope)
