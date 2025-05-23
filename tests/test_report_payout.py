import json
import pytest
from payroll.report_payout import PayoutReport, ConsoleOutput, JSONOutput

employees = [
    {"name": "Alice", "department": "HR", "hours_worked": 10, "hourly_rate": 15},
    {"name": "Bob", "department": "HR", "hours_worked": 20, "hourly_rate": 20},
    {"name": "Charlie", "department": "IT", "hours_worked": 30, "hourly_rate": 30},
]

def test_console_output_format(capsys):
    report = PayoutReport(output=ConsoleOutput())
    report.generate(employees)
    captured = capsys.readouterr().out

    assert "HR:" in captured
    assert "IT:" in captured
    assert "Alice" in captured
    assert "Charlie" in captured
    assert "total:" in captured
    assert "$" in captured

def test_json_output_format(capsys):
    report = PayoutReport(output=JSONOutput())
    report.generate(employees)
    captured = capsys.readouterr().out

    data = json.loads(captured)
    assert "HR" in data
    assert "IT" in data
    assert data["HR"][0]["name"] == "Alice"
    assert data["IT"][0]["payout"] == 900  # 30 * 30
