# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/proxy/vmess/inbound/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray.com.core.common.protocol import user_pb2 as v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/proxy/vmess/inbound/config.proto',
  package='v2ray.core.proxy.vmess.inbound',
  syntax='proto3',
  serialized_pb=_b('\n/v2ray.com/core/proxy/vmess/inbound/config.proto\x12\x1ev2ray.core.proxy.vmess.inbound\x1a)v2ray.com/core/common/protocol/user.proto\"\x1a\n\x0c\x44\x65tourConfig\x12\n\n\x02to\x18\x01 \x01(\t\"0\n\rDefaultConfig\x12\x10\n\x08\x61lter_id\x18\x01 \x01(\r\x12\r\n\x05level\x18\x02 \x01(\r\"\xd6\x01\n\x06\x43onfig\x12.\n\x04user\x18\x01 \x03(\x0b\x32 .v2ray.core.common.protocol.User\x12>\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\x0b\x32-.v2ray.core.proxy.vmess.inbound.DefaultConfig\x12<\n\x06\x64\x65tour\x18\x03 \x01(\x0b\x32,.v2ray.core.proxy.vmess.inbound.DetourConfig\x12\x1e\n\x16secure_encryption_only\x18\x04 \x01(\x08\x42P\n\"com.v2ray.core.proxy.vmess.inboundP\x01Z\x07inbound\xaa\x02\x1eV2Ray.Core.Proxy.Vmess.Inboundb\x06proto3')
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_user__pb2.DESCRIPTOR,])




_DETOURCONFIG = _descriptor.Descriptor(
  name='DetourConfig',
  full_name='v2ray.core.proxy.vmess.inbound.DetourConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='v2ray.core.proxy.vmess.inbound.DetourConfig.to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=152,
)


_DEFAULTCONFIG = _descriptor.Descriptor(
  name='DefaultConfig',
  full_name='v2ray.core.proxy.vmess.inbound.DefaultConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alter_id', full_name='v2ray.core.proxy.vmess.inbound.DefaultConfig.alter_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='v2ray.core.proxy.vmess.inbound.DefaultConfig.level', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=202,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.proxy.vmess.inbound.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='v2ray.core.proxy.vmess.inbound.Config.user', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='v2ray.core.proxy.vmess.inbound.Config.default', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detour', full_name='v2ray.core.proxy.vmess.inbound.Config.detour', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secure_encryption_only', full_name='v2ray.core.proxy.vmess.inbound.Config.secure_encryption_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=419,
)

_CONFIG.fields_by_name['user'].message_type = v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_user__pb2._USER
_CONFIG.fields_by_name['default'].message_type = _DEFAULTCONFIG
_CONFIG.fields_by_name['detour'].message_type = _DETOURCONFIG
DESCRIPTOR.message_types_by_name['DetourConfig'] = _DETOURCONFIG
DESCRIPTOR.message_types_by_name['DefaultConfig'] = _DEFAULTCONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetourConfig = _reflection.GeneratedProtocolMessageType('DetourConfig', (_message.Message,), dict(
  DESCRIPTOR = _DETOURCONFIG,
  __module__ = 'v2ray.com.core.proxy.vmess.inbound.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vmess.inbound.DetourConfig)
  ))
_sym_db.RegisterMessage(DetourConfig)

DefaultConfig = _reflection.GeneratedProtocolMessageType('DefaultConfig', (_message.Message,), dict(
  DESCRIPTOR = _DEFAULTCONFIG,
  __module__ = 'v2ray.com.core.proxy.vmess.inbound.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vmess.inbound.DefaultConfig)
  ))
_sym_db.RegisterMessage(DefaultConfig)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'v2ray.com.core.proxy.vmess.inbound.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vmess.inbound.Config)
  ))
_sym_db.RegisterMessage(Config)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.v2ray.core.proxy.vmess.inboundP\001Z\007inbound\252\002\036V2Ray.Core.Proxy.Vmess.Inbound'))
# @@protoc_insertion_point(module_scope)
