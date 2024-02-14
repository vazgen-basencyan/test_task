# Selenium Automated Login Test

This project is designed to automate testing of the login functionality for a web application. It utilizes Selenium for browser automation and Allure for generating detailed test reports. The tests cover both positive and negative login scenarios.

## Features

- Automated login functionality testing using Selenium
- Support for multiple test scenarios
- Test report generation using Allure

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip for managing Python packages

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/selenium-login-test.git
```

2. Navigate into the project directory:

```bash
cd selenium-login-test
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install Selenium, pytest, and any other dependencies needed for the project.

## Running the Tests

To run the automated tests, execute the following command in the terminal:

```bash
pytest tests/
```

### Generating Allure Reports

Ensure Allure is installed on your system. After running the tests, generate the Allure report by executing:

```bash
allure serve allure-results
```
## not implented completely because of time

This command will automatically open a web browser displaying the test reports.