const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './tests/browser',
  timeout: 30000,
  globalTimeout: 300000,
  retries: 0,
  workers: 2,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: { baseURL: 'http://127.0.0.1:8000', screenshot: 'only-on-failure', trace: 'retain-on-failure' },
  projects: ['chromium', 'firefox', 'webkit'].flatMap(browserName =>
    [320, 390, 768, 1280].map(width => ({
      name: browserName + '-' + width,
      use: { browserName, viewport: { width, height: 900 } }
    }))),
  webServer: {
    command: 'python3 -m http.server 8000 --bind 127.0.0.1 --directory frontend',
    url: 'http://127.0.0.1:8000',
    reuseExistingServer: !process.env.CI
  }
});
