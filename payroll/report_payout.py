from collections import defaultdict
import json
from abc import ABC, abstractmethod


class ReportOutput(ABC):
    @abstractmethod
    def render(self, data: dict) -> None:
        pass


class ConsoleOutput(ReportOutput):
    def render(self, data: dict) -> None:
        header = f'{"name":>17}{"hours":>22}{"rate":>21}{"payout":>21}'
        print(header)

        for department, emps in data.items():
            print(f'{department}:')
            total_hours = 0
            total_payout = 0
            for emp in emps:
                payout = emp["hours_worked"] * emp["hourly_rate"]
                total_hours += emp["hours_worked"]
                total_payout += payout
                print(f'------------ {emp["name"]:<15}'
                      f' {int(emp["hours_worked"]):>8}'
                      f' {int(emp["hourly_rate"]):>20}'
                      f' {int(payout):>20}$')
            print(f'total:{int(total_hours):>31}{int(total_payout):>43}$')
            print()


class JSONOutput(ReportOutput):
    def render(self, data: dict) -> None:
        output = {}
        for department, emps in data.items():
            output[department] = []
            for emp in emps:
                payout = emp["hours_worked"] * emp["hourly_rate"]
                output[department].append({
                    "name": emp["name"],
                    "hours_worked": int(emp["hours_worked"]),
                    "hourly_rate": int(emp["hourly_rate"]),
                    "payout": int(payout)
                })
        print(json.dumps(output, indent=4))


class PayoutReport:
    def __init__(self, output: ReportOutput = None):
        self.output = output or ConsoleOutput()

    def generate(self, employees: list) -> None:
        by_department = defaultdict(list)

        for emp in employees:
            by_department[emp["department"]].append(emp)
        self.output.render(by_department)
