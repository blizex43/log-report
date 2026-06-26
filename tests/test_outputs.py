from pathlib import Path
import json


def load():
    return json.loads(Path("/app/report.json").read_text())


def test_report_exists():
    """Success Criterion: report.json exists at /app/report.json"""
    assert Path("/app/report.json").exists()


def test_report_schema():
    """Success Criterion: report contains required fields"""
    data = load()
    assert "total_requests" in data
    assert "unique_ips" in data
    assert "top_path" in data


def test_report_values_basic():
    """Success Criterion: report values are valid types and non-empty"""
    data = load()

    assert isinstance(data["total_requests"], int)
    assert isinstance(data["unique_ips"], int)
    assert isinstance(data["top_path"], str)

    assert data["total_requests"] > 0
    assert data["unique_ips"] > 0