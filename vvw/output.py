#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division

try:
    import ujson as json
except ImportError:
    import json

from .pocket import get_pocket
from . import op
from .utils import json_encoded


@json_encoded
def generate_vvw_timeline():
    pocket = get_pocket()
    line = op.get_timeline(pocket)

    items = []
    for item in line:
        tmp = item.copy()
        tmp['topics'] = op.extract_topic(item['text'])

        items.append(tmp)

    return {'items': items, }


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
