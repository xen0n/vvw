#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division

import os
import re

from jieba.analyse import extract_tags

AT_ELIMINATION_RE = re.compile(r'[@][^\s]+')
TAG_COUNT = 5


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
