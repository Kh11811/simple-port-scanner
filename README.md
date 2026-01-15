
# Simple TCP Port Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-lightgrey?style=flat-square)

A lightweight, zero-dependency command-line network scanner built in Python. This tool allows security enthusiasts and administrators to check for open TCP ports on a target host within a user-defined range.

##  Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Legal Disclaimer](#-legal-disclaimer)
- [License](#-license)

##  Features

- **Zero Dependencies:** Built entirely using Python's standard `sys` and `socket` libraries.
- **Customizable Range:** Users can define the specific port range (1 to N) to scan.
- **Error Handling:** Gracefully handles socket errors and connection timeouts.
- **Cross-Platform:** Works on Linux, Windows, and macOS.

##  Prerequisites

Ensure you have Python installed on your system.

```bash
python3 --version
# Should return Python 3.x

```

##  Installation

1. **Clone the repository** (or download the script):
```bash
git clone https://github.com/Kh11811/simple-port-scanner

```


2. **Navigate to the directory**:
```bash
cd simple-port-scanner

```



##  Usage

Run the script directly from the terminal. The script requires two arguments: the **target host** and the **maximum port** to scan.

### Syntax

```bash
python3 scanner.py <TARGET_HOST> <MAX_PORT>

```

### Examples

**Scan a local server for ports 1 to 100:**

```bash
python3 scanner.py 127.0.0.1 100

```

**Scan a remote IP for ports 1 to 1024:**

```bash
python3 scanner.py 192.168.1.5 1024

```

### Sample Output

```text
port 22 is open
port 80 is open
port 443 is open

```

##  Legal Disclaimer

**Please Read Carefully:**

> This tool is intended for **educational purposes** and **authorized security auditing** only.
> Scanning networks or systems without the explicit permission of the owner is illegal in many jurisdictions and may violate your Internet Service Provider's Terms of Service. The author and contributors of this project accept no responsibility for unauthorized or malicious use of this software.
