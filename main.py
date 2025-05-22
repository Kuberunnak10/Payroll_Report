import argparse
from payroll.parser import parse_employees
from payroll.report_payout import PayoutReport

# Список отчетов
REPORTS = {
    "payout": PayoutReport,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="CSV файл с данными о работниках.")
    parser.add_argument("--report", required=True, help="Тип отчета.")
    args = parser.parse_args()
    report_class = REPORTS.get(args.report)

    if not report_class:
        raise ValueError(f"Отчета '{args.report}' не существует.")

    employees = []

    for file_path in args.files:
        employees.extend(parse_employees(file_path))

    report = report_class()
    report.generate(employees)


if __name__ == "__main__":
    main()
