
# CloudOps Sentinel

## Python & Linux Infrastructure Health Monitor

CloudOps Sentinel is a small Python project that checks the health of a Linux system.

The main goal is simple: collect system information, check disk usage, give a clear status, create a JSON report, and save logs.

The project also includes automated tests and GitHub Actions to run the tests automatically.

---

## What does it do?

CloudOps Sentinel:

- gets the Linux hostname
- checks disk usage
- compares disk usage with configured limits
- returns `OK`, `WARNING` or `CRITICAL`
- creates a JSON report
- saves execution logs
- runs automated tests
- uses GitHub Actions for Continuous Integration

Example:

```text

How it works
Linux System
     |
     v
main.py
     |
     v
system_checker.py
     |
     v
Check hostname + disk usage
     |
     v
OK / WARNING / CRITICAL
     |
     v
report.py
     |
     v
JSON Report
     |
     v
Logs
     |
     v
Automated Tests
     |
     v
GitHub Actions

Project Structure
cloudops-sentinel/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── screenshots/
│   ├── 01-project-structure.png
│   ├── 02-tests-system-checker.png
│   ├── 03-json-report.png
│   ├── 04-tests-passing.png
│   ├── 05-main-and-logging.png
│   └── 06-github-actions-success.png
│
├── src/
│   ├── config.py
│   ├── report.py
│   └── system_checker.py
│
├── tests/
│   ├── test_report.py
│   └── test_system_checker.py
│
├── logs/
├── reports/
│
├── config.json
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

Technologies
- Python 3
- Linux
- JSON
- pathlib
- subprocess
- logging
- unittest
- Git
- GitHub
- GitHub Actions
The project uses Python standard libraries, so there are currently no external Python packages to install.
Disk Monitoring
The disk limits are stored in config.json.
{
    "disk_warning": 80,
    "disk_critical": 90,
    "aws_enabled": false
}

The disk status works like this:
Below 80%       -> OK
80% - 89%       -> WARNING
90% or higher   -> CRITICAL

This means the limits can be changed in the configuration file without changing the main Python logic.
Linux Commands
The project uses Python subprocess to run Linux commands.
Hostname:
hostname

Disk usage:
df -h /

The Python code reads the command output and uses it to check the system status.
JSON Report
After the check, the project creates:
reports/system_report.json

Example:
{
    "hostname": "DESKTOP-B090PPP",
    "disk_used_percent": 1,
    "disk_status": "OK"
}

The report is simple and can be easily read by another program or automation tool.
Logging
The project also creates a log file:
logs/cloudops-sentinel.log

Example:
2026-10-06 19:08:15,024 - INFO - System check started
2026-10-06 19:08:15,026 - INFO - System check completed
2026-10-06 19:08:15,026 - INFO - Report created

This gives a simple history of what the application did.
Error Handling
The project uses Python try and except to handle possible errors.
For example, if a Linux command fails or the command output is not in the expected format, the program can return an error status instead of simply stopping.
Testing
The project uses Python's built-in unittest module.
To run all tests:
python -m unittest discover -s tests -v

Current tests check:
- disk status OK
- disk status WARNING
- disk status CRITICAL
- JSON report creation
Current result:
test_create_report ... ok
test_disk_status_critical ... ok
test_disk_status_ok ... ok
test_disk_status_warning ... ok

----------------------------------------------------------------------
Ran 4 tests

OK

GitHub Actions
The project uses GitHub Actions for Continuous Integration.
Every time code is pushed to GitHub, the workflow runs the tests automatically.
The workflow is:
git push
   |
   v
GitHub
   |
   v
GitHub Actions
   |
   v
Ubuntu Linux
   |
   v
Python
   |
   v
Run tests
   |
   v
PASS / FAIL

The workflow file is:
.github/workflows/ci.yml

The current CI workflow successfully runs all 4 tests.
Installation
Clone the repository:
git clone https://github.com/Mohib416/cloudops-sentinel.git

Enter the project:
cd cloudops-sentinel

Create a virtual environment:
python3 -m venv .venv

Activate it:
source .venv/bin/activate

Usage
Run the system check:
python main.py

Run the tests:
python -m unittest discover -s tests -v

What I Practiced With This Project
This project helped me practice several basic Cloud and DevOps skills:
- Python scripting
- Linux commands
- Linux system monitoring
- Python functions
- dictionaries
- JSON configuration
- file handling
- pathlib
- subprocess
- error handling
- logging
- automated testing
- Git
- GitHub
- GitHub Actions
- Continuous Integration
Project Goal
I built CloudOps Sentinel as a practical project to connect Python and Linux with basic DevOps practices.
The idea was to keep the project simple and understandable while still using a real workflow:
Collect data
     ↓
Analyze data
     ↓
Create report
     ↓
Save logs
     ↓
Run tests
     ↓
Push to GitHub
     ↓
GitHub Actions checks the project

Screenshots
Project Structure

System Checker Tests

JSON Report

All Tests Passing

Main Program and Logging

GitHub Actions

Future Improvements
Some possible improvements for a future version are:
- CPU monitoring
- memory monitoring
- network checks
- more Linux health checks
- better reports
- optional AWS integration
- alert notifications
These features are not part of the current version.
Project Status
Completed
CloudOps Sentinel currently includes Linux monitoring, disk health checks, JSON configuration, JSON reports, logging, automated tests, Git/GitHub and GitHub Actions CI.
```
System check completed.
Status: OK
Report: reports/system_report.json
