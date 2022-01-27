AUTHOR = 'Ryan Asher'
SITENAME = "Ryan Asher"
SITEURL = 'https://ryandeanasher.com'
THEME = "C:/Users/ryanasher/Documents/Projects/pelican-themes/nice-blog"
SIDEBAR_ABOUT = "Hi! I enjoy learning and creating. You can find some of my writing on this website, and some of the small games I've developed."
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']

PATH = 'content'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True