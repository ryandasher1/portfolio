AUTHOR = 'Ryan Asher'
SITENAME = "Ryan Asher"
#SITEURL = 'https://ryandeanasher.com/'
SITEURL = 'http://127.0.0.1:8000'
THEME = "../pelican-themes/pelican-fh5co-marble"

PLUGINS_PATH = ['../pelican-paths']
PLUGINS = [
    'i18n_subsites',
    'tipue_search'
]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

PATH = 'content'

LOGO = '/images/ryanface.jpg'

STATIC_PATHS = [
    'images',
    'extra'
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

HERO = [
    {
        'image': '/images/hero/randomized_stratego_2.jpg',
        'title': "Hi, I'm Ryan!",
        'text': "I'm an award-winning engineer with over a decade of experience in the media industry. In my spare time I like to write short stories and make simple videogames!",
        'links': [
        # {
        #     'url': '/resume.pdf',
        #     'text': 'Resume'
        # }
    ]
    }
]
DISQUS_ON_PAGES = False

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
  ('Twitter', 'https://twitter.com/ryandeanasher'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True