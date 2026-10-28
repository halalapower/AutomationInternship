# GetTop E2E Test Suite (QA Automation Internship)

BDD end-to-end tests for [gettop.us](https://gettop.us), a WooCommerce demo store, written during a QA automation internship (2022). Each scenario maps to a ticket from the internship board (for example TMTN-108, TMTN-123, TMTN-144).

**Stack:** Python · Selenium 4 · Behave (Gherkin) · Page Object Model

## What's covered
| Feature | Scenarios |
|---|---|
| Top banner carousel | Next/previous arrows and pagination dots change the featured product |
| Accessories menu | Menu shows the expected items; each item opens the right product page |
| Search | *Work in progress (`@wip`), skipped by default* |

## Project layout
```
automation_internship/
├── app/application.py      # wires page objects onto the Behave context
├── pages/                  # Page Object Model (base page, main page, header, product page)
├── features/
│   ├── environment.py      # browser setup and teardown per scenario
│   ├── steps/              # step definitions (shared steps in common_steps.py)
│   └── tests/*.feature     # Gherkin scenarios
└── behave.ini              # skips @wip scenarios by default
```

## Run it
```bash
pip install -r requirements.txt
cd automation_internship
python -m behave                                   # Chrome, visible window
HEADLESS=1 python -m behave                        # headless
BROWSER=firefox HEADLESS=1 python -m behave        # Firefox
python -m behave --tags=@wip                       # include work-in-progress scenarios
```
No driver downloads are needed: Selenium Manager (Selenium 4.6+) fetches the matching ChromeDriver or GeckoDriver.

## Notes
- The suite was written against the 2022 version of the site. Locators may need updating where the store's layout has changed since.
- 2026 cleanup: removed committed driver binaries and IDE files, fixed browser setup order, merged duplicate step definitions, fixed the left-arrow step and the accessories locator, and switched to Selenium Manager.
