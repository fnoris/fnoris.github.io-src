# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Noris Fabio'
SITENAME = 'Noris Fabio'
SITESUBTITLE = 'infosec addict, coder, free thinker'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/norisfabio'),
          ('github', 'https://github.com/fnoris'),
          ('envelope', 'mailto:info@norisfabio.com'))


# THEME = '/home/nrs/Coding/Websites/pelican-themes/Flex'
THEME = 'attila'

# Pagination
DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

HEADER_COVER = 'assets/images/intro-bg.jpg'

# Post and Pages path 
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path 
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

SHOW_CREDITS = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

### Plugins

PLUGIN_PATHS = [
  '/home/nrs/Coding/Websites/pelican-plugins'
  ]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets'
]

# Sitemap
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


### Theme specific settings

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/nrs.css']

AUTHORS_BIO = {
  "noris fabio": {
    "name": "Noris Fabio",
    "cover": "assets/images/intro-bg.jpg",
    "image": "assets/images/avatar.png",
    "website": "https://www.norisfabio.com",
    "location": "Italy",
    "bio": "infosec addict, coder, free thinker"
  }
}

