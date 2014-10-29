from jinja2 import Environment, PackageLoader
import os

JINJA_ENV = Environment(loader=PackageLoader('wellknown', 'templates'))

LINKS = [
    {
        "rel": "lrdd",
        "template": "https://%s/musterroll/webfinger/jrd?resource={uri}" % os.getenv("CLOUDFLEET_HOST", "example.com")
    }
]

