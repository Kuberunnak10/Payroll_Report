from payroll.report_payout import PayoutReport


def test_generate_output(capsys):
    employees = [
        {"name": "Alice", "department": "Marketing", "hours_worked": 160, "hourly_rate": 50},
        {"name": "Bob", "department": "Design", "hours_worked": 150, "hourly_rate": 40},
    ]

    report = PayoutReport()
    report.generate(employees)

    captured = capsys.readouterr()
    assert "Marketing" in captured.out
    assert "Design" in captured.out
    assert "Alice" in captured.out
    assert "Bob" in captured.out
