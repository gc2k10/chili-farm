# Frontend demo

A standalone responsive dashboard using synthetic data only. No backend, credentials or device controls are required.

From the repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory frontend
```

Visit http://127.0.0.1:8000. The period selector changes the synthetic history chart. Stop the server with Ctrl+C.

See [quick start](../docs/demo-start.md), [validation scope and results](../docs/demo-validation.md) and [release notes](../docs/releases/v0.1.0-demo.md). This is not a production dashboard.

## Run browser checks

Node.js 22 and npm are needed only for development tests, not for running the demo.

```sh
npm install --ignore-scripts --package-lock=false
npx playwright install --with-deps chromium firefox webkit
npm test
```

Run these commands from the repository root. Browser/dependency installation may need additional system permissions on Linux. Reports are saved in playwright-report and test-results.
