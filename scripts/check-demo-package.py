#!/usr/bin/env python3
"""Verify the complete demo archive, hashes and locally served asset links."""
import hashlib
import json
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Thread
from urllib.parse import urljoin
from urllib.request import urlopen
from zipfile import ZipFile

root = Path(__file__).resolve().parents[1]
brand = json.loads((root / "tests/browser/brand.json").read_text())
slug = brand["repository"].rsplit("/", 1)[1]
archive = root / "dist" / (slug + "-v0.1.0-demo.zip")
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        target = attrs.get("src") or attrs.get("href")
        if target and not target.startswith(("https:", "http:", "#")):
            self.targets.append(target)

with TemporaryDirectory(prefix="demo-check-") as folder:
    with ZipFile(archive) as bundle:
        names = bundle.namelist()
        assert len(names) == len(set(names)) == 13, names
        assert all(not Path(n).is_absolute() and ".." not in Path(n).parts for n in names)
        manifest = json.loads(bundle.read("manifest.json"))
        assert manifest["synthetic_data_only"] is True
        assert set(names) == set(manifest["sha256"]) | {"manifest.json"}
        for name, digest in manifest["sha256"].items():
            assert hashlib.sha256(bundle.read(name)).hexdigest() == digest, name
        bundle.extractall(folder)
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=folder))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        base = "http://127.0.0.1:" + str(server.server_port) + "/"
        for page in ["index.html", "about.html"]:
            with urlopen(base + page) as response:
                parser = Links()
                parser.feed(response.read().decode())
            for target in parser.targets:
                with urlopen(urljoin(base + page, target)) as response:
                    assert response.status == 200, target
                    assert response.read(), target
        print("Verified: 13 allowlisted files, manifest hashes, local HTTP pages and assets")
    finally:
        server.shutdown()
        server.server_close()
