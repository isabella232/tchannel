from __future__ import absolute_import

from .types import Types
from .call_request import CallRequestMessage


class CallResponseMessage(CallRequestMessage):
    """Respond to an RPC call."""
    message_type = Types.CALL_RES

    __slots__ = (
        'flags',
        'ttl',

        # Zipkin-style tracing data
        'span_id',
        'parent_id',
        'trace_id',

        'traceflags',
        'service',
        'headers',
    )