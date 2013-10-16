#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division

from functools import wraps

try:
    import ujson as json
except ImportError:
    import json


def json_encoded(fn):
    @wraps(fn)
    def _wrapped_(*args, **kwargs):
        result = fn(*args, **kwargs)

        return json.dumps(result)

    return _wrapped_


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
