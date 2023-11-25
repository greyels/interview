import unittest

from url_shortener import URLShortener


class TestURLShortener(unittest.TestCase):
    def test_store_url(self):
        url_to_store = "https://www.revolut.com/rewards-personalised-cashback-and-discounts/"
        url_shortener = URLShortener()
        short_url = url_shortener.store_url(url_to_store)
        self.assertEqual(url_to_store, url_shortener.url_map[short_url])

    def test_get_original_url(self):
        url_to_store = "https://www.revolut.com/rewards-personalised-cashback-and-discounts/"
        url_shortener = URLShortener()
        short_url = url_shortener.store_url(url_to_store)
        original_url = url_shortener.get_original_url(short_url)
        self.assertEqual(url_to_store, original_url)

    def test_url_not_found(self):
        short_url = "asd4df"
        # with self.assertRaises(KeyError):
        #     URLShortener().get_original_url(short_url)
        self.assertRaises(KeyError, URLShortener().get_original_url, short_url)
