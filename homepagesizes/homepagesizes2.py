import urllib.request
import time
start_time = time.time()


sites = [
    'https://www.yahoo.com/',
    'http://www.cnn.com',
    'http://www.python.org',
    'http://www.jython.org',
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
    'http://www.macrumors.com/',
    'http://arstechnica.com/',
    'http://www.reuters.com/',
    'http://abcnews.go.com/',
    'http://www.cnbc.com/',
]

def sitesize(url):
    ''' Determine the size of a website '''
    with urllib.request.urlopen(url) as u:
        page = u.read()
        return url, len(page)

for result in map(sitesize, sites):
    print(result)

print("--- %s seconds ---" % (time.time() - start_time))