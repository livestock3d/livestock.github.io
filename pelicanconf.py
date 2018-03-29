import datetime

AUTHOR = 'Christian Kongsgaard'
SITENAME = 'Livestock3D'
SITEURL = 'https://livestock3d.github.io'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

# Top menus
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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
AUTHOR_AVATAR = 'https://github.com/livestock3d/livestock3d.github.io/blob/master/images/profil.jpg'
AUTHOR_WEB = 'http://ocni-dtu.github.io'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
#PLUGINS = ['']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

