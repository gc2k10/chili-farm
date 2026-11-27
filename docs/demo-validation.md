# ChiliFarm demo validation

Date: 27 November 2026 (Europe/Warsaw).

## Automated browser checks

Release gate: all 60 checks must pass with retries disabled before a draft is created or updated. The draft release links the workflow result for its exact source commit. Earlier successful runs were followed by an intermittent WebKit observer-loop error during the release gate; this was fixed by responding to viewport resize events instead of observing SVG mutations.

Playwright 1.65.1 runs Chromium, Firefox and WebKit at viewport widths of 320, 390, 768 and 1280 pixels (900 pixels high). These are desktop browser engines with resized viewports, not physical phones/tablets or a claim of full Safari/iOS compatibility.

Each browser/width combination checks:

- Dashboard and presentation load; approved logo dimensions and proportions are preserved.
- No document-wide horizontal overflow; local links and assets return successful responses.
- Favicon and Apple icon declarations exist; page loading makes no external requests and emits no JavaScript page errors.
- The period selector changes the chart and live summary, then restores the initial series.
- Dashboard/presentation navigation and expected source/support destinations.
- Axis labels retain at least 11.9 rendered pixels and the period selector is at least 44 pixels high; repeated resizing preserves the selected period without JavaScript errors.

The report and screenshots are retained by GitHub Actions for 14 days. The release-draft workflow reruns this suite against its exact commit before preparing a draft.

## Observed correction

The original fixed 600-unit chart reduced axis labels to about 6 pixels at a 320-pixel viewport. Chart coordinates now adapt to the available width without changing synthetic values. The period control previously measured 34 pixels high and now has a 44-pixel minimum. Keyboard focus is explicitly outlined.

## Other checks and limits

Both GitHub Pages deployments completed successfully after the fix. Repository documentation checks passed. Public-page checks confirmed the corrected VaultPanel chart at 320 pixels, period changes and keyboard focus. Original logo geometry is unchanged.

No hardware, production backend, payment flow, physical mobile devices, screen-reader audit or full-history secret scan was tested. External support destination availability does not prove payment processing. This evidence supports a static demo prerelease only.
