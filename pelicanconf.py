# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = 'Hydpy'
SITENAME = 'HydPy'
SITEURL = ''  # Intentionally left blank, see ./publishconf.py

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

INDEX_SAVE_AS = 'article_home.html'
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

DEFAULT_PAGINATION = 10

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

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

# Theme settings --------------------------------------------------------------

THEME = 'themes/pelican-alchemy/alchemy'

#SITESUBTITLE = 'A magical \u2728 Pelican theme'
SITESUBTITLE = 'Community driven group for promoting python in Hyderabad.'
SITEIMAGE = '/images/profile.jpg width=200 height=200'
DESCRIPTION = 'Hyderabad Python User group is growing and active Python user community in Hyderabad.'\
              'We believe in Knowledge is power, community is strength!!!'\
              'Meet other local Python developers, learners, employers, and enthusiasts of all kinds.'\
              'All skill levels are welcome: if you are interested in Python, we are interested in you!'

LINKS = (
    ('PythonExpress', 'https://pythonexpress.in/'),
    ('pssi.org.in', 'https://pssi.org.in/'),
    #('Jinja2', 'http://jinja.pocoo.org/'),
)

ICONS = [
    ('github', 'https://github.com/HydPy/'),
    ('facebook', 'https://www.facebook.com/HydPy/'),
    ('meetup', 'https://www.meetup.com/Hyderabad-Python-Meetup-Group/'),
]

PYGMENTS_STYLE = 'monokai'
RFG_FAVICONS = True

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
