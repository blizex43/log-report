# Log Report

Parse an Apache-style access log and generate a structured JSON report.

## Overview

This project processes access logs and extracts key metrics into a JSON report containing:

- **total_requests**: The number of non-empty lines in the log
- **unique_ips**: Count of unique IP addresses (first whitespace-separated token per line)
- **top_path**: The most frequently requested URL path from HTTP requests

## Directory Structure

```
log-report/
├── instruction.md          # Task requirements and definitions
├── task.toml               # Task configuration
├── solution/
│   ├── solve.py           # Main solution script
│   └── solve.sh           # Solution entry point
├── tests/
│   ├── test_outputs.py    # Test suite
│   └── test.sh            # Test runner
├── environment/
│   ├── Dockerfile         # Container definition
│   └── solution_hint.py   # Reference implementation
└── jobs/                  # Historical run results
```

## Usage

### Run the solution

```bash
./solution/solve.sh
```

This reads `/app/access.log` and writes the report to `/app/report.json`.

### Run tests

```bash
./tests/test.sh
```

Executes pytest on the test suite and generates verification output.

### Run with harbor

```bash
harbor run -p . --agent oracle
```

## Input/Output

**Input**: `/app/access.log` (Apache-style access log)

**Output**: `/app/report.json` (JSON with required fields)

### Example Output

```json
{
	"total_requests": 1000,
	"unique_ips": 45,
	"top_path": "/api/users"
}
```

## Requirements

- Python 3
- Valid JSON output with exactly three fields
- All values must match the log file analysis

## Reward System

When running with `harbor run`:

- **Reward 1**: Tests pass (pytest exit code 0)
- **Reward 0**: Tests fail
