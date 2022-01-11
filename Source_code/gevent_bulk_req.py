from __future__ import print_function
import gevent
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()
import requests

# Note that we're using HTTPS, so
# this demonstrates that SSL works.
urls = [
    'https://www.google.com/',
    'https://www.apple.com/',
    'https://www.python.org/',
    "http://www.apple.com",
    "http://www.microsoft.com",
    "http://www.amazon.com", 
    "http://www.facebook.com",
    "http://www.crickbuzz.com",

]



def print_head(url):
    print('Starting %s' % url)
    data = requests.get(url).text
    print('%s: %s bytes: %r' % (url, len(data), data[:50]))

jobs = [gevent.spawn(print_head, f"https://emperor2.dimabusiness.com/dns/url?url={_url}") for _url in urls]

gevent.wait(jobs)