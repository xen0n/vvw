#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division

import os
import re

from jieba.analyse import extract_tags

AT_ELIMINATION_RE = re.compile(r'[@][^\s]+')
TIMELINE_RESULT_LIMIT = 100
TAG_COUNT = 5


def read_timeline(channel):
    return channel.home_timeline(TIMELINE_RESULT_LIMIT)


def mix_timelines(lines):
    tmp = []
    for line in lines:
        # reverse-chronological order
        #tmp.extend((-item['time'], item, ) for item in line)
        for item in get_parsed(line):
            tmp.append((-item['time'], item, ))

    return [item[1] for item in sorted(tmp)]


def get_timeline(pocket):
    return mix_timelines(read_timeline(chan) for chan in pocket.values())


def get_parsed(l):
    for item in l:
        yield item['parsed']


def preprocess_item(item):
    result = item.copy()
    result['text'] = AT_ELIMINATION_RE.sub('', item['text'])

    return result


def extract_topic(text):
    return extract_tags(text, TAG_COUNT)


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
