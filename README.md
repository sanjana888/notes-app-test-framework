ExpandTesting Notes Applicarion/Manual and Automation Testing Project.

## Project Overview

This project has been developed with a view to applying manual testing and automation testing techniques to test the ExpandTesting Notes Application.

The project includes:
- Manual testing documentation
- UI automation testing
- API automation testing
- Validation - Hybrid UI + API
- Parallel execution support
- Reporting and validation of performance

The primary objective of this project is to validate the functionality of the Notes app and create the Automation Project with Selenium web driver with Python using Pytest.

---

## Application Under Test

### UI Application
https://practice.expandtesting.com/notes/app/login

### API Documentation
https://practice.expandtesting.com/notes/api/api-docs/

---

# Section 1 — Manual Testing

## Manual Testing Activities

The following manual testings activities were performed:

- Requirement analysis
- Manual test planning
- Test scenario preparation
- Test case preparation
- Test data preparation
- Test execution tracking
- Defect reporting
- Requirement Traceability Matrix (RTM)
- Test summary reporting

---

## Manual Testing Documents

There are the following manual testing documents in the project (in excel format):

- Test Plan
- Test Scenarios
- Test Cases
- Test Data
- Test Execution Report
- Requirement Traceability Matrix
- Defect Report
- Test Summary Report
- Key Metrics

---

## Manual Testing Coverage

These are the following functionalities that were manually tested:

- Login functionality
- Generates a note in the UI.
- Ensure that notes are visible in the UI.
- This is the API validation command
- Validation from UI to API data.
- Remove note using API.
- Synchronization between API and UI.
- Negative UI validations
- Negative API validations

---

The section introduces you to the concept of UI Automation, API Automation, and Hybrid Testing.The section will introduce you to what is UI Automation, API Automation and Hybrid Testing.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Requests Library
- WebDriver Manager
- Pytest-xdist
- Allure Reporting
- YAML Configuration

---
# Section 3 — Advanced Topics

## Parallel Execution
pytest-xdist is used to run tests in parallel.

Command:
pytest -n 3

There are pytests fixtures for each test that provide its own webdriver.

## Selenium Grid
There exists a Docker version of Selenium Grid that can be used.

Command:
You have to install the selenium/standalone-chrome image and then start it on port 4444 (as selenium-grid).

## CI/CD Jenkins
Jenkins pipeline includes:
1. Checkout source code
2. Install dependencies
3. Test parallelism-test anything at the same time.
4. Generate Allure report
5. Save screen shots, logs and reports

## Agentic Automation
Agentic features include:
- Self-healing locators
- Retry mechanism
- Smart waits
- Failure analysis support

## MCP Layer
MCP support includes:
- Generates the test data using LLM technology.
- LLM-assisted failure analysis
- Locator suggestion helper

## Performance Engineering
Performance checks include:
- Validates the response time of the API.
- Wait time until UI is loaded.
- Enables CSV logs to be plotted over time.

## Final Deliverables
- Manual test plan
Use test scenarios and test cases to check computer program(s) for correct results.
- RTM
- Test using Selenium Python Pytest framework.
- Test automation of UI and API.
- Allure report
- Jenkinsfile
- Parallel execution support
---

## Automation Framework Structure

```text
Project/
│
├── tests/
│   ├── test_login.py
│   ├── test_notes_ui.py
│   ├── test_api.py
│   ├── test_hybrid.py
│   └── test_performance.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── notes_page.py
│
├── fixtures/
│   └── browser_fixture.py
│
├── config/
│   ├── config.yaml
│   └── environment.py
│
├── utils/
│   ├── api_client.py
│   ├── logger.py
│   ├── retry.py
│   ├── self_healing.py
│   ├── smart_wait.py
│   ├── mcp_utils.py
│   └── performance_utils.py
│
├── ci_cd/
│   └── Jenkinsfile
│
├── grid/
│   └── selenium_grid_setup.txt
│
├── reports/
├── screenshots/
│
├── requirements.txt
├── pytest.ini
├── conftest.py
├── .gitignore
└── README.md