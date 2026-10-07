# CloudOps Sentinel

### Python & Linux Infrastructure Health Monitor

[![CloudOps Sentinel CI](https://github.com/Mohib416/cloudops-sentinel/actions/workflows/ci.yml/badge.svg)](https://github.com/Mohib416/cloudops-sentinel/actions/workflows/ci.yml)

CloudOps Sentinel is a lightweight Python-based infrastructure health monitoring tool designed to automate basic Linux system checks.

The application collects system information, analyzes disk usage against configurable thresholds, generates a JSON health report, records execution logs, and automatically runs tests through GitHub Actions.

The project was built to demonstrate practical Python, Linux, automation, testing, Git, GitHub, and Continuous Integration skills relevant to Cloud and DevOps environments.

---

## 🚀 Features

- Linux system information collection
- Hostname detection
- Disk usage monitoring
- Configurable disk thresholds
- Health status classification:
  - `OK`
  - `WARNING`
  - `CRITICAL`
- JSON configuration
- JSON report generation
- Error handling
- Application logging
- Automated testing with `unittest`
- Git version control
- GitHub repository
- GitHub Actions Continuous Integration

---

## 🏗️ Architecture

```text
                    Linux System
                         |
                         v
                      main.py
                         |
                         v
                 system_checker.py
                         |
              +----------+----------+
              |                     |
              v                     v
           hostname             disk usage
                                  |
                                  v
                         Health Analysis
                                  |
                    +-------------+-------------+
                    |             |             |
                    v             v             v
                   OK          WARNING       CRITICAL
                    |             |             |
                    +-------------+-------------+
                                  |
                                  v
                              report.py
                                  |
                                  v
                         JSON System Report
                                  |
                                  v
                         Logging / Monitoring
                                  |
                                  v
                         Automated Testing
                                  |
                                  v
                         GitHub Actions CI
