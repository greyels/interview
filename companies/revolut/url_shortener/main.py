import random
import string

from flask import Flask, request, redirect


class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, original_url):
        short_url = self.generate_short_url()
        self.url_map[short_url] = original_url
        return short_url

    @staticmethod
    def generate_short_url(length=6):
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(length))


app = Flask(__name__)
url_shortener = URLShortener()


@app.route("/shorten", methods=["POST"])
def shorten():
    orig_url = request.form.get("orig_url")
    if not orig_url:
        return "Invalid URL", 400

    short_url = url_shortener.shorten_url(orig_url)
    return f"Shorten URL: {request.url_root}{short_url}"


@app.route("/<short_url>", methods=["GET"])
def redirect_url(short_url):
    orig_url = url_shortener.url_map.get(short_url)
    if not orig_url:
        return "URL not found", 404
    return redirect(orig_url)


if __name__ == '__main__':
    app.run(debug=True)
