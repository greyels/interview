# Requirements:
# Should accept incoming POST requests to create short format of incoming url and add it to the DB
# Should accept incoming GET requests with long url and redirect those requests to original url
import unittest

from main import url_shortener, app


class TestURLShortener(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_shorten_url(self):
        orig_url = "https://verylongurlhere.longlong"
        short_url = url_shortener.shorten_url(orig_url)
        self.assertEqual(orig_url, url_shortener.url_map[short_url])

        long_url = url_shortener.url_map[short_url]
        self.assertEqual(orig_url, long_url)

        response = self.client.post("/shorten", data={"orig_url": orig_url})
        self.assertEqual(200, response.status_code)
        self.assertIn(b"Shorten URL", response.data)

    def test_redirect_url(self):
        orig_url = "https://verylongurlhere.longlong"
        short_url = "rthn56n"
        url_shortener.url_map[short_url] = orig_url

        redirect_response = self.client.get(f"/{short_url}")
        self.assertEqual(302, redirect_response.status_code)
        self.assertEqual(orig_url, redirect_response.location)

    def test_invalid_url(self):
        response = self.client.post("/shorten", data={"orig_url": ""})
        self.assertEqual(400, response.status_code)
        self.assertIn(b"Invalid URL", response.data)

    def test_url_not_found(self):
        response = self.client.get("/non-existing_url")
        self.assertEqual(404, response.status_code)
        self.assertIn(b"URL not found", response.data)


if __name__ == '__main__':
    unittest.main()
