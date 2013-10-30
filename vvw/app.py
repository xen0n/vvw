#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division

from weiyu.shortcuts import *
from weiyu.utils.decorators import only_methods

from .pocket import get_pocket
from .output import generate_vvw_timeline


class RenrenStatusID(object):
    def __init__(self, id, uid):
        self.status_id = id
        self.source_user_id = uid


@http
@jsonview
def timeline_view(request):
    return 200, generate_vvw_timeline(), {}


@http
@jsonview
@only_methods(['POST', ])
def reply_view(request, platform, id, uid):
    id, uid = int(id), int(uid)
    text = request.form['content']

    # prepare status ID object
    if platform == 'RenrenStatus':
        statusID = RenrenStatusID(id, uid)
    else:
        # TODO
        raise NotImplementedError

    p = get_pocket()
    result = 99999
    for chan in p.itervalues():
        if chan.platform == platform:
            result = chan.reply(statusID, text)
            break

    return 200, {'status': result, }, {}


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
