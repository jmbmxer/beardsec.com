#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jimmy'
SITENAME = 'beardsec'
SITEURL = 'http://beardsec.com'
PAGE_DIR = 'content/pages'
WITH_FUTURE_DATES = False
RELATIVE_URLS = False
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
TYPOGRIFY = False
THEME = './themes/SoMA'

FEED_RSS = 'rss.xml'
#$CATEGORY_FEED_RSS = '%s/rss.xml'
CATEGORY_FEED_ATOM = None

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.htm'

#GOOGLE_ANALYTICS = '< YOUR GA CODE >'

#PLUGINS=['plugins.sitemap', 'plugins.gzip_cache']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_PAGINATION = 10
