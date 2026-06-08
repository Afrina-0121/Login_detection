# Failed Login Detection

## Overview

Failed Login Detection is a Python-based cybersecurity project that analyzes authentication log files and identifies failed login attempts. The project helps detect suspicious login activity and potential brute-force attacks by monitoring repeated authentication failures.

## Features

- Reads and analyzes log files
- Detects failed login attempts
- Counts failed attempts for each user
- Generates alerts when a user exceeds a defined threshold
- Simple and lightweight implementation using Python
- Easy to customize for different log formats

## Project Structure

```text
failed-login-detection/
│
├── auth.log
├── login_detection.py
└── README.md
```

## Sample Log Format

```text
INFO User admin logged in successfully
FAILED User Asha login failed
FAILED User Asha login failed
FAILED User Asha login failed
INFO User alice logged in successfully
FAILED User Sheela login failed
FAILED User Sheela login failed
```

## How It Works

1. Reads the log file line by line.
2. Identifies entries marked as `FAILED`.
3. Counts failed login attempts for each user.
4. Generates an alert when the number of failed attempts exceeds the threshold.
5. Displays the results to the user.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/afrina-0121/login-detection.git
```

2. Navigate to the project directory:

```bash
cd failed-login-detection
```

## Requirements

- Python 3.x

Check your Python version:

```bash
python3 --version
```

## Usage

Run the script:

```bash
python3 Login_detection.py
```

Example Output:

```text
Asha : 3
ALERT: Asha has multiple failed logins

Sheela : 2
```

## Cybersecurity Concepts Used

- Log Analysis
- Authentication Monitoring
- Threat Detection
- Security Event Monitoring
- Brute Force Attack Detection
- Python Automation

## Future Enhancements

- Real-time log monitoring
- Email alert notifications
- Dashboard for visualization
- IP address tracking
- CSV report generation

## Learning Outcomes

This project provides hands-on experience in:

- Python programming
- File handling
- Data processing
- Log analysis
- Cybersecurity monitoring
- Security incident detection

## Author

Afrina M

Cybersecurity Student | Python Learner | Aspiring Security Analyst

## License

This project is intended for educational and learning purposes.
