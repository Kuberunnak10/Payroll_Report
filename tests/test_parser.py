import pytest
from payroll.parser import parse_employees


def test_parse_employees(tmp_path):
    # Создаем временный CSV-файл
    csv_content = """name,department,hours_worked,hourly_rate
Alice,Marketing,160,50
Bob,Design,150,40
"""
    file = tmp_path / "employees.csv"
    file.write_text(csv_content)

    employees = parse_employees(str(file))
    assert len(employees) == 2
    assert employees[0]["name"] == "Alice"
    assert employees[1]["department"] == "Design"
    assert employees[0]["hours_worked"] == 160.0
    assert employees[1]["hourly_rate"] == 40.0


def test_parse_employees_missing_rate(tmp_path):
    csv_content = "name,department,hours_worked\nAlice,Marketing,160\n"
    file = tmp_path / "bad.csv"
    file.write_text(csv_content)

    with pytest.raises(ValueError):
        parse_employees(str(file))
