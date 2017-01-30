#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hélène'
SITENAME = 'Data science w/ a geo bias'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Beirut'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
}

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup','pelican-bootstrapify','related_posts']#,'pelican-toc']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

TOC = {
    'TOC_HEADERS' : '^h[1-2]',  # What headers should be included in the generated toc
                                # Expected format is a regular expression

    'TOC_RUN'     : 'false'      # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}


#MARKDOWN = ['toc']

# For the related post plugin
RELATED_POSTS_MAX = 10

# Theme settings --------------------------------------------------------------

THEME = 'themes/alchemy'

SITESUBTITLE = 'Hélène Draux'
SITEIMAGE = '/images/compass2.png width=100 height=100'
DESCRIPTION = 'Portfolio with data science projects and visualisation'

LINKS = (
    ('www', 'http://www.helenedraux.net/'),
)

ICONS = [
    ('github', 'https://github.com/helenedraux'),
]

PYGMENTS_STYLE = 'lovelace'
RFG_FAVICONS = True

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

DEFAULT_DATE_FORMAT = '%d %B %Y'
HIDE_AUTHORS = True

DISPLAY_PAGES_ON_MENU = True

GOOGLE_ANALYTICS = 'UA-90338324-1'

HIDE_CATEGORY = True

DISQUS_SITENAME = "helenedraux-github-io"

#For the tag cloud
import math
JINJA_FILTERS = {
    'count_to_font_size': lambda c: '{p:.1f}%'.format(p=100 + 25 * math.log(c, 2)),
}