# Selenium Python Automation Framework

This repository contains a Selenium-based automation framework designed to simplify browser-based testing using Python. It provides a robust and extendable framework for running comprehensive test suites.

## Features

- **Page Object Model (POM):** Utilizes the POM design pattern for better maintainability and readability of the code.
- **Multi-Browser Support:** Compatible with major browsers like Chrome, Firefox, and Edge.
- **Reporting:** Integrated reporting with tools like Allure or ExtentReports for clear and detailed test results.
- **Parallel Execution:** Supports parallel test execution to reduce runtime.
- **Configurable:** Easy configuration setup to manage different environments and testing scenarios.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python (3.8 or newer)
- Selenium WebDriver
- WedDriverManager
- PyTest
- Allure report
- html Report
- log
= Data-Driven

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:kartikeya27/PythonSeleniumFramework.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd PythonSeleniumFramework
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirement.txt
   ```
### Configuration

Edit the config.json file in the root directory to set up your testing environment, browsers, and other preferences.

### Running Tests

To run tests, execute the following command from the root directory:

```bash
pytest --cache-clear -v --browser chrome --url https://www.yatra.com/ --alluredir=reports/allure-results
```

### Directory Structure
```bash
├── README.md
├── assets
├── automation.log
├── base
├── configfiles
├── env
├── myenv
├── pages
├── reports
├── requirement.txt
├── testcases
├── testdata
├── utilities
└── venv
```

### To generate the Allure report please follow below steps
```bash
pytest --cache-clear -v --browser chrome --url https://www.yatra.com/ --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
allure serve reports/allure-results
```