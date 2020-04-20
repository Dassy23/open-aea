# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rail_stomp.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="rail_stomp.proto",
    package="fetch.aea.RailStomp",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x10rail_stomp.proto\x12\x13\x66\x65tch.aea.RailStomp"\xf3\t\n\x10RailStompMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12W\n\x0crail_updates\x18\x05 \x01(\x0b\x32?.fetch.aea.RailStomp.RailStompMessage.Rail_Updates_PerformativeH\x00\x1a\x9c\x01\n\tEventType\x12Q\n\nevent_type\x18\x01 \x01(\x0e\x32=.fetch.aea.RailStomp.RailStompMessage.EventType.EventTypeEnum"<\n\rEventTypeEnum\x12\x0b\n\x07\x41RRIVAL\x10\x00\x12\r\n\tDEPARTURE\x10\x01\x12\x0f\n\x0b\x44\x45STINATION\x10\x02\x1a\xbe\x01\n\x0fVariationStatus\x12\x63\n\x10variation_status\x18\x01 \x01(\x0e\x32I.fetch.aea.RailStomp.RailStompMessage.VariationStatus.VariationStatusEnum"F\n\x13VariationStatusEnum\x12\x0b\n\x07ON_TIME\x10\x00\x12\t\n\x05\x45\x41RLY\x10\x01\x12\x08\n\x04LATE\x10\x02\x12\r\n\tOFF_ROUTE\x10\x03\x1a\xa7\x05\n\x19Rail_Updates_Performative\x12\x43\n\nevent_type\x18\x01 \x01(\x0b\x32/.fetch.aea.RailStomp.RailStompMessage.EventType\x12O\n\x10variation_status\x18\x02 \x01(\x0b\x32\x35.fetch.aea.RailStomp.RailStompMessage.VariationStatus\x12\x1a\n\x12planned_event_type\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x18\n\x10planned_datetime\x18\x05 \x01(\t\x12\x17\n\x0f\x61\x63tual_datetime\x18\x06 \x01(\t\x12"\n\x1aplanned_timetable_datetime\x18\x07 \x01(\t\x12\x10\n\x08location\x18\x08 \x01(\t\x12\x17\n\x0flocation_stanox\x18\t \x01(\x05\x12\x15\n\ris_correction\x18\n \x01(\x08\x12\x18\n\x10train_terminated\x18\x0b \x01(\x08\x12\x19\n\x11operating_company\x18\x0c \x01(\t\x12\x15\n\rdivision_code\x18\r \x01(\t\x12\x1a\n\x12train_service_code\x18\x0e \x01(\t\x12\x10\n\x08train_id\x18\x0f \x01(\t\x12\x14\n\x0cis_off_route\x18\x10 \x01(\x08\x12\x18\n\x10\x63urrent_train_id\x18\x11 \x01(\t\x12\x19\n\x11original_location\x18\x12 \x01(\t\x12\x34\n,original_location_planned_departure_datetime\x18\x13 \x01(\t\x12\x14\n\x0cminutes_late\x18\x14 \x01(\x05\x12\x1e\n\x16\x65\x61rly_late_description\x18\x15 \x01(\tB\x0e\n\x0cperformativeb\x06proto3'
    ),
)


_RAILSTOMPMESSAGE_EVENTTYPE_EVENTTYPEENUM = _descriptor.EnumDescriptor(
    name="EventTypeEnum",
    full_name="fetch.aea.RailStomp.RailStompMessage.EventType.EventTypeEnum",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ARRIVAL", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DEPARTURE", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DESTINATION", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=358,
    serialized_end=418,
)
_sym_db.RegisterEnumDescriptor(_RAILSTOMPMESSAGE_EVENTTYPE_EVENTTYPEENUM)

_RAILSTOMPMESSAGE_VARIATIONSTATUS_VARIATIONSTATUSENUM = _descriptor.EnumDescriptor(
    name="VariationStatusEnum",
    full_name="fetch.aea.RailStomp.RailStompMessage.VariationStatus.VariationStatusEnum",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ON_TIME", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="EARLY", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="LATE", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="OFF_ROUTE", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=541,
    serialized_end=611,
)
_sym_db.RegisterEnumDescriptor(_RAILSTOMPMESSAGE_VARIATIONSTATUS_VARIATIONSTATUSENUM)


_RAILSTOMPMESSAGE_EVENTTYPE = _descriptor.Descriptor(
    name="EventType",
    full_name="fetch.aea.RailStomp.RailStompMessage.EventType",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="event_type",
            full_name="fetch.aea.RailStomp.RailStompMessage.EventType.event_type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_RAILSTOMPMESSAGE_EVENTTYPE_EVENTTYPEENUM,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=262,
    serialized_end=418,
)

_RAILSTOMPMESSAGE_VARIATIONSTATUS = _descriptor.Descriptor(
    name="VariationStatus",
    full_name="fetch.aea.RailStomp.RailStompMessage.VariationStatus",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="variation_status",
            full_name="fetch.aea.RailStomp.RailStompMessage.VariationStatus.variation_status",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_RAILSTOMPMESSAGE_VARIATIONSTATUS_VARIATIONSTATUSENUM,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=421,
    serialized_end=611,
)

_RAILSTOMPMESSAGE_RAIL_UPDATES_PERFORMATIVE = _descriptor.Descriptor(
    name="Rail_Updates_Performative",
    full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="event_type",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.event_type",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="variation_status",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.variation_status",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="planned_event_type",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.planned_event_type",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="status",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.status",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="planned_datetime",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.planned_datetime",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="actual_datetime",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.actual_datetime",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="planned_timetable_datetime",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.planned_timetable_datetime",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.location",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="location_stanox",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.location_stanox",
            index=8,
            number=9,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="is_correction",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.is_correction",
            index=9,
            number=10,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="train_terminated",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.train_terminated",
            index=10,
            number=11,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="operating_company",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.operating_company",
            index=11,
            number=12,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="division_code",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.division_code",
            index=12,
            number=13,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="train_service_code",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.train_service_code",
            index=13,
            number=14,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="train_id",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.train_id",
            index=14,
            number=15,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="is_off_route",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.is_off_route",
            index=15,
            number=16,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="current_train_id",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.current_train_id",
            index=16,
            number=17,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="original_location",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.original_location",
            index=17,
            number=18,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="original_location_planned_departure_datetime",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.original_location_planned_departure_datetime",
            index=18,
            number=19,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="minutes_late",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.minutes_late",
            index=19,
            number=20,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="early_late_description",
            full_name="fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative.early_late_description",
            index=20,
            number=21,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=614,
    serialized_end=1293,
)

_RAILSTOMPMESSAGE = _descriptor.Descriptor(
    name="RailStompMessage",
    full_name="fetch.aea.RailStomp.RailStompMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.RailStomp.RailStompMessage.message_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_starter_reference",
            full_name="fetch.aea.RailStomp.RailStompMessage.dialogue_starter_reference",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_responder_reference",
            full_name="fetch.aea.RailStomp.RailStompMessage.dialogue_responder_reference",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="fetch.aea.RailStomp.RailStompMessage.target",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="rail_updates",
            full_name="fetch.aea.RailStomp.RailStompMessage.rail_updates",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _RAILSTOMPMESSAGE_EVENTTYPE,
        _RAILSTOMPMESSAGE_VARIATIONSTATUS,
        _RAILSTOMPMESSAGE_RAIL_UPDATES_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.RailStomp.RailStompMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=42,
    serialized_end=1309,
)

_RAILSTOMPMESSAGE_EVENTTYPE.fields_by_name[
    "event_type"
].enum_type = _RAILSTOMPMESSAGE_EVENTTYPE_EVENTTYPEENUM
_RAILSTOMPMESSAGE_EVENTTYPE.containing_type = _RAILSTOMPMESSAGE
_RAILSTOMPMESSAGE_EVENTTYPE_EVENTTYPEENUM.containing_type = _RAILSTOMPMESSAGE_EVENTTYPE
_RAILSTOMPMESSAGE_VARIATIONSTATUS.fields_by_name[
    "variation_status"
].enum_type = _RAILSTOMPMESSAGE_VARIATIONSTATUS_VARIATIONSTATUSENUM
_RAILSTOMPMESSAGE_VARIATIONSTATUS.containing_type = _RAILSTOMPMESSAGE
_RAILSTOMPMESSAGE_VARIATIONSTATUS_VARIATIONSTATUSENUM.containing_type = (
    _RAILSTOMPMESSAGE_VARIATIONSTATUS
)
_RAILSTOMPMESSAGE_RAIL_UPDATES_PERFORMATIVE.fields_by_name[
    "event_type"
].message_type = _RAILSTOMPMESSAGE_EVENTTYPE
_RAILSTOMPMESSAGE_RAIL_UPDATES_PERFORMATIVE.fields_by_name[
    "variation_status"
].message_type = _RAILSTOMPMESSAGE_VARIATIONSTATUS
_RAILSTOMPMESSAGE_RAIL_UPDATES_PERFORMATIVE.containing_type = _RAILSTOMPMESSAGE
_RAILSTOMPMESSAGE.fields_by_name[
    "rail_updates"
].message_type = _RAILSTOMPMESSAGE_RAIL_UPDATES_PERFORMATIVE
_RAILSTOMPMESSAGE.oneofs_by_name["performative"].fields.append(
    _RAILSTOMPMESSAGE.fields_by_name["rail_updates"]
)
_RAILSTOMPMESSAGE.fields_by_name[
    "rail_updates"
].containing_oneof = _RAILSTOMPMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["RailStompMessage"] = _RAILSTOMPMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RailStompMessage = _reflection.GeneratedProtocolMessageType(
    "RailStompMessage",
    (_message.Message,),
    dict(
        EventType=_reflection.GeneratedProtocolMessageType(
            "EventType",
            (_message.Message,),
            dict(
                DESCRIPTOR=_RAILSTOMPMESSAGE_EVENTTYPE,
                __module__="rail_stomp_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.RailStomp.RailStompMessage.EventType)
            ),
        ),
        VariationStatus=_reflection.GeneratedProtocolMessageType(
            "VariationStatus",
            (_message.Message,),
            dict(
                DESCRIPTOR=_RAILSTOMPMESSAGE_VARIATIONSTATUS,
                __module__="rail_stomp_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.RailStomp.RailStompMessage.VariationStatus)
            ),
        ),
        Rail_Updates_Performative=_reflection.GeneratedProtocolMessageType(
            "Rail_Updates_Performative",
            (_message.Message,),
            dict(
                DESCRIPTOR=_RAILSTOMPMESSAGE_RAIL_UPDATES_PERFORMATIVE,
                __module__="rail_stomp_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.RailStomp.RailStompMessage.Rail_Updates_Performative)
            ),
        ),
        DESCRIPTOR=_RAILSTOMPMESSAGE,
        __module__="rail_stomp_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.RailStomp.RailStompMessage)
    ),
)
_sym_db.RegisterMessage(RailStompMessage)
_sym_db.RegisterMessage(RailStompMessage.EventType)
_sym_db.RegisterMessage(RailStompMessage.VariationStatus)
_sym_db.RegisterMessage(RailStompMessage.Rail_Updates_Performative)


# @@protoc_insertion_point(module_scope)
