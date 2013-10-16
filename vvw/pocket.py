#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division

import os

from snsapi.snspocket import SNSPocket

CONF_PATH = '../conf/channels.json'
CONF_ABS_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), CONF_PATH))


def _do_get_pocket(_sp_cache=[]):
    if _sp_cache:
        return _sp_cache[0]

    sp = SNSPocket()
    sp.load_config(CONF_ABS_PATH)
    sp.auth()
    _sp_cache.append(sp)
    return sp


def get_pocket():
    return _do_get_pocket()


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
