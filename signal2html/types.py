# -*- coding: utf-8 -*-

"""Utilities for dealing with message types

These are extracted from the Signal Android app source code.

License: See LICENSE file.

"""

BASE_TYPE_MASK = 0x1F

INCOMING_CALL_TYPE = 1
OUTGOING_CALL_TYPE = 2
MISSED_CALL_TYPE = 3
JOINED_TYPE = 4
UNSUPPORTED_MESSAGE_TYPE = 5
INVALID_MESSAGE_TYPE = 6

GROUP_CALL_TYPE = 12

GROUP_CTRL_TYPE_BIT = 0x10000
GROUP_V2_DATA_TYPE_BIT = 0x80000

BASE_INBOX_TYPE = 20
BASE_OUTBOX_TYPE = 21
BASE_SENDING_TYPE = 22
BASE_SENT_TYPE = 23
BASE_SENT_FAILED_TYPE = 24
BASE_PENDING_SECURE_SMS_FALLBACK = 25
BASE_PENDING_INSECURE_SMS_FALLBACK = 26
BASE_DRAFT_TYPE = 27

OUTGOING_MESSAGE_TYPES = [
    BASE_OUTBOX_TYPE,
    BASE_SENT_TYPE,
    BASE_SENDING_TYPE,
    BASE_SENT_FAILED_TYPE,
    BASE_PENDING_SECURE_SMS_FALLBACK,
    BASE_PENDING_INSECURE_SMS_FALLBACK,
]


def is_outgoing_message_type(_type):
    for outgoingType in OUTGOING_MESSAGE_TYPES:
        if _type & BASE_TYPE_MASK == outgoingType:
            return True
    return False


def is_inbox_type(_type):
    return _type & BASE_TYPE_MASK == BASE_INBOX_TYPE


def is_incoming_call(_type):
    return _type == INCOMING_CALL_TYPE


def is_outgoing_call(_type):
    return _type == OUTGOING_CALL_TYPE


def is_missed_call(_type):
    return _type == MISSED_CALL_TYPE


def is_group_call(_type):
    return _type == GROUP_CALL_TYPE


def is_group_ctrl(_type):
    return _type & GROUP_CTRL_TYPE_BIT == GROUP_CTRL_TYPE_BIT


def is_group_v2_data(_type):
    return _type & GROUP_V2_DATA_TYPE_BIT == GROUP_V2_DATA_TYPE_BIT


def is_joined_type(_type):
    return _type & BASE_TYPE_MASK == JOINED_TYPE


def get_named_message_type(_type):
    if is_group_ctrl(_type):
        if is_group_v2_data(_type):
            return "group-update-v2"
        else:
            return "group-update-v1"
    if is_outgoing_message_type(_type):
        return "outgoing"
    elif is_inbox_type(_type):
        return "incoming"
    elif is_incoming_call(_type):
        return "call-incoming"
    elif is_outgoing_call(_type):
        return "call-outgoing"
    elif is_missed_call(_type):
        return "call-missed"
    elif is_group_call(_type):
        return "group-call"
    elif is_joined_type(_type):
        return "joined"
    return "unknown"
