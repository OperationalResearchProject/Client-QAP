# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0emessages.proto\"\x84\x01\n\x16InitTransactionRequest\x12\x10\n\x08\x63ustomer\x18\x01 \x01(\t\x12\x14\n\x0csolutionSize\x18\x02 \x01(\x05\x12\x0f\n\x07\x66itness\x18\x03 \x01(\x01\x12\x10\n\x08solution\x18\x04 \x01(\t\x12\x11\n\talgorithm\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\"I\n\x16GenericFitnessResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08solution\x18\x02 \x01(\t\x12\x11\n\titeration\x18\x03 \x01(\x05\"F\n\x15GenericFitnessRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x66itness\x18\x02 \x01(\x01\x12\x10\n\x08solution\x18\x03 \x01(\t\"S\n\x14MultiFitnessResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1c\n\tsolutions\x18\x02 \x03(\x0b\x32\t.Solution\x12\x11\n\titeration\x18\x03 \x01(\x05\"R\n\x13MultiFitnessRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfitnesses\x18\x02 \x03(\x01\x12\x1c\n\tsolutions\x18\x03 \x03(\x0b\x32\t.Solution\"*\n\x0bStopRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"=\n\x0cStopResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08solution\x18\x02 \x01(\t\x12\x0f\n\x07\x66itness\x18\x03 \x01(\x01\"u\n\x08Solution\x12\x17\n\x0fmother_solution\x18\x01 \x01(\t\x12\x16\n\x0emother_fitness\x18\x06 \x01(\x01\x12\x10\n\x08mother_i\x18\x02 \x01(\x05\x12\x10\n\x08mother_j\x18\x03 \x01(\x05\x12\t\n\x01i\x18\x04 \x01(\x05\x12\t\n\x01j\x18\x05 \x01(\x05\x62\x06proto3')
)




_INITTRANSACTIONREQUEST = _descriptor.Descriptor(
  name='InitTransactionRequest',
  full_name='InitTransactionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer', full_name='InitTransactionRequest.customer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solutionSize', full_name='InitTransactionRequest.solutionSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fitness', full_name='InitTransactionRequest.fitness', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solution', full_name='InitTransactionRequest.solution', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='InitTransactionRequest.algorithm', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='InitTransactionRequest.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=19,
  serialized_end=151,
)


_GENERICFITNESSRESPONSE = _descriptor.Descriptor(
  name='GenericFitnessResponse',
  full_name='GenericFitnessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GenericFitnessResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solution', full_name='GenericFitnessResponse.solution', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iteration', full_name='GenericFitnessResponse.iteration', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=153,
  serialized_end=226,
)


_GENERICFITNESSREQUEST = _descriptor.Descriptor(
  name='GenericFitnessRequest',
  full_name='GenericFitnessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GenericFitnessRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fitness', full_name='GenericFitnessRequest.fitness', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solution', full_name='GenericFitnessRequest.solution', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=228,
  serialized_end=298,
)


_MULTIFITNESSRESPONSE = _descriptor.Descriptor(
  name='MultiFitnessResponse',
  full_name='MultiFitnessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MultiFitnessResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solutions', full_name='MultiFitnessResponse.solutions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iteration', full_name='MultiFitnessResponse.iteration', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=300,
  serialized_end=383,
)


_MULTIFITNESSREQUEST = _descriptor.Descriptor(
  name='MultiFitnessRequest',
  full_name='MultiFitnessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MultiFitnessRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fitnesses', full_name='MultiFitnessRequest.fitnesses', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solutions', full_name='MultiFitnessRequest.solutions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=385,
  serialized_end=467,
)


_STOPREQUEST = _descriptor.Descriptor(
  name='StopRequest',
  full_name='StopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='StopRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='StopRequest.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=469,
  serialized_end=511,
)


_STOPRESPONSE = _descriptor.Descriptor(
  name='StopResponse',
  full_name='StopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='StopResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solution', full_name='StopResponse.solution', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fitness', full_name='StopResponse.fitness', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=513,
  serialized_end=574,
)


_SOLUTION = _descriptor.Descriptor(
  name='Solution',
  full_name='Solution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mother_solution', full_name='Solution.mother_solution', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mother_fitness', full_name='Solution.mother_fitness', index=1,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mother_i', full_name='Solution.mother_i', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mother_j', full_name='Solution.mother_j', index=3,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i', full_name='Solution.i', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='j', full_name='Solution.j', index=5,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=576,
  serialized_end=693,
)

_MULTIFITNESSRESPONSE.fields_by_name['solutions'].message_type = _SOLUTION
_MULTIFITNESSREQUEST.fields_by_name['solutions'].message_type = _SOLUTION
DESCRIPTOR.message_types_by_name['InitTransactionRequest'] = _INITTRANSACTIONREQUEST
DESCRIPTOR.message_types_by_name['GenericFitnessResponse'] = _GENERICFITNESSRESPONSE
DESCRIPTOR.message_types_by_name['GenericFitnessRequest'] = _GENERICFITNESSREQUEST
DESCRIPTOR.message_types_by_name['MultiFitnessResponse'] = _MULTIFITNESSRESPONSE
DESCRIPTOR.message_types_by_name['MultiFitnessRequest'] = _MULTIFITNESSREQUEST
DESCRIPTOR.message_types_by_name['StopRequest'] = _STOPREQUEST
DESCRIPTOR.message_types_by_name['StopResponse'] = _STOPRESPONSE
DESCRIPTOR.message_types_by_name['Solution'] = _SOLUTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitTransactionRequest = _reflection.GeneratedProtocolMessageType('InitTransactionRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITTRANSACTIONREQUEST,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:InitTransactionRequest)
  ))
_sym_db.RegisterMessage(InitTransactionRequest)

GenericFitnessResponse = _reflection.GeneratedProtocolMessageType('GenericFitnessResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERICFITNESSRESPONSE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:GenericFitnessResponse)
  ))
_sym_db.RegisterMessage(GenericFitnessResponse)

GenericFitnessRequest = _reflection.GeneratedProtocolMessageType('GenericFitnessRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERICFITNESSREQUEST,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:GenericFitnessRequest)
  ))
_sym_db.RegisterMessage(GenericFitnessRequest)

MultiFitnessResponse = _reflection.GeneratedProtocolMessageType('MultiFitnessResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTIFITNESSRESPONSE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:MultiFitnessResponse)
  ))
_sym_db.RegisterMessage(MultiFitnessResponse)

MultiFitnessRequest = _reflection.GeneratedProtocolMessageType('MultiFitnessRequest', (_message.Message,), dict(
  DESCRIPTOR = _MULTIFITNESSREQUEST,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:MultiFitnessRequest)
  ))
_sym_db.RegisterMessage(MultiFitnessRequest)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), dict(
  DESCRIPTOR = _STOPREQUEST,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:StopRequest)
  ))
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), dict(
  DESCRIPTOR = _STOPRESPONSE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:StopResponse)
  ))
_sym_db.RegisterMessage(StopResponse)

Solution = _reflection.GeneratedProtocolMessageType('Solution', (_message.Message,), dict(
  DESCRIPTOR = _SOLUTION,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Solution)
  ))
_sym_db.RegisterMessage(Solution)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
