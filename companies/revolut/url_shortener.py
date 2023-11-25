# A URL shortener is a service to generate,
# retrieve and delete short URLs mapped to original URLs
# (e.g.: http://goo.gl , URL Shortener - Short URLs & Custom Free Link Shortener | Bitly  etc.)
# The goal is to create a library that allows managing URL shortening, similar to URL Shortener -
# Short URLs & Custom Free Link Shortener | Bitly .

# Input:
# https://www.revolut.com/rewards-personalised-cashback-and-discounts/
#
# Expected output:
# https://www.rev.me/<url identifier>
#
# reqs:
# Should get long url and store it in memory/map
# Should accept short url
# Should return long url related to accepted short url


import random

import string


class URLShortener:
    def __init__(self):
        self.url_map = {}

    def store_url(self, original_url):
        short_url = self.generate_short_url(original_url)
        self.url_map[short_url] = original_url
        return short_url

    @staticmethod
    def generate_short_url(length=6):
        chars = string.ascii_letters + string.digits
        short_url = "".join(random.choice(chars) for _ in range(length))
        return short_url

    def get_original_url(self, short_url):
        return self.url_map[short_url]
