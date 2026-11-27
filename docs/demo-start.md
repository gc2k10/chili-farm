# ChiliFarm demo — Quick start

This package is a standalone demonstration with synthetic data. It does not connect to sensors, servers, storage or payment systems and cannot control hardware.

## Run the downloaded demo package

1. Extract the entire ZIP into a new directory. Keep the assets directory beside index.html.
2. Open a terminal in that extracted directory.
3. With Python 3 installed, run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

4. Open http://127.0.0.1:8000 in your browser.
5. Use Period to switch between 24 hours and 7 days. Open About the project to view the presentation.
6. Stop the server with Ctrl+C.

No Python packages, Node.js, database, account, credentials or device access are required to run the demo. The server listens on this computer only. If port 8000 is occupied, use 8001 and open the matching address.

## Run from the repository

From the repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory frontend
```

The demo is also available at https://gc2k10.github.io/chili-farm/.

## Expected behavior and limitations

All readings and status messages are predefined examples, not live measurements. The chart period changes only the sample series. There is no backend, authentication, persistence, installation service or device control. This is a prerelease demo, not a production management application.

If images are missing, verify that the ZIP was fully extracted and that assets/brand exists. If old branding appears online, reload without the browser cache. Physical-device testing and assistive-technology testing are not covered by the automated browser matrix.

## Verify the package

SHA256SUMS accompanies the download. On macOS run `shasum -a 256 <archive-name>.zip`; on Linux run `sha256sum <archive-name>.zip` and compare the result. manifest.json records the source commit and SHA-256 of each packaged file.
