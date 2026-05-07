ExpandTesting Notes Application is a manual and automation testing project.

## Project Overview

The aim of this project is to carry out manual testing and automation testing on the ExpandTesting Notes Application.

The project includes:
- Manual testing documentation
- UI automation testing
- API automation testing
- Forced validation of UI + API.
- Negative testing
- Parallel execution support
- Selenium Grid integration
- Docker integration
- Jenkins CI/CD integration
- Allure & HTML reporting
- MCP/LLM-based automation concepts
- Performance validation

The goal of this project is to test the functionality of Notes Application and to create a scalable automation framework with Selenium WebDriver and Python/Pytest.

---

# Application Under Test

## UI Application
https://practice.expandtesting.com/notes/app/login

## API Documentation
https://practice.expandtesting.com/notes/api/api-docs/

---

# Section 1 — Manual Testing

## Manual Testing Activities

These are the manual testing activities carried out:

- Requirement analysis
- Manual test planning
- Test scenario preparation
- Test case preparation
- Test data preparation
- Test execution tracking
- Defect reporting
- Requirement Traceability Matrix (RTM).
- Test summary reporting

---

## Manual Testing Documents

There are the following manual test documents in the project (in Excel format):

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

These are the functions that have been manually tested:

- Login functionality
- Create note using UI.
- Confirm whether or not notes are visible in UI
- API validation is performed on Notes.
- Validates UI and API data.
- Remove a note by using the API.
- Send request from API to UI synchronously.
- Negative UI validations
- Negative API validations

---

This section covers the automation of the UI and API, along with Hybrid Testing.This section focuses on UI Automation, API Automation and Hybrid Testing.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Requests Library
- Pytest-xdist
- Docker
- Jenkins
- Allure Reporting
- Pytest-HTML
- YAML Configuration

---

# Automation Framework Structure

# Automation Framework Structure

Project/
│
├── tests/
│   ├── test_login.py
│   ├── test_notes_ui.py
│   ├── test_api.py
│   ├── test_hybrid.py
│   ├── test_negative_login.py
│   ├── test_negative_api.py
│   ├── test_negative_notes.py
│   ├── test_negative_ui.py
│   ├── test_parallel_demo.py
│   ├── test_performance.py
│   └── test_mcp_demo.py
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
├── drivers/
│
├── requirements.txt
├── pytest.ini
├── conftest.py
├── .gitignore
└── README.md

# UI Automation Coverage

## Positive Test Cases
- Valid login
- Click on the Create note button to create a note, with the data you have provided.
- Ensure that notes are visible in UI.
- Validate for valid notes to be created.

## Negative Test Cases
- Invalid login
- Use the "Create note" option to create a note that doesn't have a title.
- Invalid page access

---

# API Automation Coverage

## Positive Test Cases
- API validation is performed on Notes.
- Validates notes with DELETE /notes API.
- API response validation

## Negative Test Cases
- Invalid token validation
- Unauthorized API access

---

# Hybrid UI + API Testing

- During UI validation of an API call.
- Create note, add to UI.
- Validate same note in API response to get notes
The API validates the content of page.
This will remove the note from the current database by using the API.
- Validate note added back to UI

---

# Reporting

The framework supports:
- Allure Reporting
- HTML Reporting
- Screenshot on failure.
- Execution logging

---

# Section 3 — Advanced Topics

## Parallel Execution

pytest-xdist is used for implementing parallel execution.

Command:

pytest -n 2

Pytest workers have their own WebDriver instance.

---

# Selenium Grid

Selenium Grid is run on Docker containers.

Supports:
- Distributed execution
- Parallel execution
- Multiple browser nodes

Grid URL:
http://localhost:4444

---

# Docker Integration

Docker is used for:
- Selenium Grid setup
- Containerized execution
- Scalable test execution

---

# Jenkins CI/CD Integration

Jenkins pipeline includes:
1. Checkout source code
2. Install dependencies
3. Perform tests concurrently
4. Generate Allure report
5. Once ready, publish screenshots, logs and reports.

---

# Agentic Automation Features

The benefits of agentic automation are:
- Self-healing locators
- Retry mechanism
- Smart waits
- Failure analysis support

---

# MCP / LLM Layer

MCP support includes:
- Using test data to generate a set of tests using LLM.- Test data generation using LLM.
- LLM-assisted failure analysis
- Intelligent suggestion helper for locating a place.

---

# Performance Engineering

Performance checks include:
- A way to validate the API response time.
- Validates the pages of the UI.
- Execution trend logging

---

# Commands to Execute

Run a complete test suite.Run a complete suite of tests.

pytest

---

## Run Parallel Execution

pytest -n 2

---

## Generate HTML Report

pytest --html=reports/report.html --self-contained-html

---

## Generate Allure Report


pytest --alluredir=reports/allure-results

allure serve reports/allure-results

---

# Selenium Grid Execution

## Start Selenium Hub

docker start selenium-hub

---

## Run Chrome Node

docker run -d --net grid -e SE_EVENT_BUS_HOST=selenium-hub -e SE_EVENT_BUS_PUBLISH_PORT=4442 -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 selenium/node-chrome

---

## Open Selenium Grid

http://localhost:4444

---

# Jenkins Execution

## Open Jenkins

http://localhost:8080

---

# Final Deliverables

- Manual Test Plan
- Test Scenarios & Test Cases
- Requirement Traceability Matrix (RTM)
- This is the Selenium "Python Pytest Framework".
- UI & API Automation
- Hybrid Testing
- Allure Report
- Jenkinsfile
- Parallel Execution Support

---

# Key Features

This is known as the Page Object Model or POM.
- Reusable Framework
- Explicit Waits
- Retry Mechanism
- Smart Wait Handling
- Parallel Execution
- Selenium Grid
- Docker Support
- Jenkins CI/CD
- Reporting Integration
- Hybrid Testing
- Performance Validation

---

# Conclusion

This project is successful in showing:
- Manual Testing
- UI Automation
- API Automation
- Hybrid UI/API Validation
- Negative Testing
- Parallel Execution
- Selenium Grid
- Docker Integration
- Jenkins CI/CD
- Reporting
- MCP/LLM Concepts
- Performance Validation

The framework is modular, scalable, reusable and maintainable.