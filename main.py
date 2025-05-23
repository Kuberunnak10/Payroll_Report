import argparse
from payroll.parser import parse_employees
from payroll.report_payout import PayoutReport, ConsoleOutput, JSONOutput

# Список отчетов
REPORTS = {
    "payout": PayoutReport,
}

# Список форматов вывода
OUTPUT_FORMATS = {
    "console": ConsoleOutput,
    "json": JSONOutput,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="CSV файл с данными о работниках.")
    parser.add_argument("--report", required=True, help="Тип отчета.")
    parser.add_argument("--format", default="console", help="Формат вывода (console, json).")
    args = parser.parse_args()

    report_class = REPORTS.get(args.report)
    if not report_class:
        raise ValueError(f"Отчета '{args.report}' не существует.")

    output_class = OUTPUT_FORMATS.get(args.format)
    if not output_class:
        raise ValueError(f"Формат вывода '{args.format}' не поддерживается.")

    employees = []
    for file_path in args.files:
        employees.extend(parse_employees(file_path))

    report = report_class(output=output_class())
    report.generate(employees)

if __name__ == "__main__":
    main()
