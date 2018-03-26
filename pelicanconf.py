import datetime

AUTHOR = 'Christian Kongsgaard'
SITENAME = 'Livestock3D'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins']

# Theme
THEME = 'pelican-themes/MinimalXY'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2018
MINIMALXY_CURRENT_YEAR = datetime.date.today().year

# Author
AUTHOR_INTRO = u'Hi everybody! Welcome to Livestock3D!'
AUTHOR_DESCRIPTION = u"I'm a former Master Student of the Technical University of Denmark (DTU)." \
                     u"\nI'm developed Livestock for my thesis."
AUTHOR_AVATAR = 'contents/images/profile.jpg'
AUTHOR_WEB = 'http://ocni-dtu.github.io'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
#PLUGINS = ['']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

