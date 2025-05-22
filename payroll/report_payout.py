class PayoutReport:
    def generate(self, employees: list) -> None:
        by_department: dict = {}

        for emp in employees:
            department = emp["department"]
            if department not in by_department:
                by_department[department] = []

            by_department[department].append(emp)

        header = f'{"name":>17}{"hours":>22}{"rate":>21}{"payout":>21}'
        print(header)

        for dep, emps in by_department.items():

            print(f'{dep}:')
            total_hours = 0
            total_payout = 0
            for emp in emps:
                payout = emp["hours_worked"] * emp["hourly_rate"]
                total_hours += emp["hours_worked"]
                total_payout += payout
                print(
                    f'------------ {emp["name"]:<15}'
                    f' {int(emp["hours_worked"]):>8}'
                    f' {int(emp["hourly_rate"]):>20}'
                    f' {int(payout):>20}$'
                )
            print(f'total:{int(total_hours):>31}{int(total_payout):>43}$')
            print()
