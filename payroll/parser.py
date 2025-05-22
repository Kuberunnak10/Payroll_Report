def parse_employees(file_path: str) -> list:
    employees = []
    with open(file_path, 'r', encoding="utf-8") as file:
        header = file.readline().strip().split(",")
        rate_field = [name for name in ["hourly_rate", "rate", "salary"] if name in header]
        if not rate_field:
            raise ValueError(f"Не найдено поле зарплаты в файле: {file_path}")

        index = {name: i for i, name in enumerate(header)}
        #print(idx)
        for line in file:

            if not line.strip():
                continue
            row = line.strip().split(",")
            #print(row)

            employees.append({
                "name": row[index["name"]],
                "department": row[index["department"]],
                "hours_worked": float(row[index["hours_worked"]]),
                "hourly_rate": float(row[index[''.join(rate_field)]]),
            })
    return employees
