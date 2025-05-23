# Payroll Report

Проект для генерации отчета по заработной плате сотрудников из CSV-файлов с выводом по отделам.

## Возможности

- Чтение CSV-файлов с разной структурой поля зарплаты (`hourly_rate`, `rate`, `salary`);
- Генерация отчета по выплатам (`--report payout`);
- Работа полностью через Docker;
- Тесты с покрытием кода (`pytest + pytest-cov`);

---

## Использование с Docker

### 1. Сборка Docker-образа

```bash
docker build -t payroll_app .
```

### 2. Запуск приложения
Вариант запуска в формате таблицы:
```bash
docker run -it --rm payroll_app python3 main.py data/data1.csv data/data2.csv data/data3.csv --report payout
```
Вариант запуска в формате json:
```bash
docker run -it --rm payroll_app python3 main.py data/data1.csv data/data2.csv data/data3.csv --report payout --format json
```

### 3. Запуск тестов
```bash
docker run -it --rm payroll_app pytest -s -v

docker run -it --rm payroll_app pytest --cov=payroll tests/
```
### Заметки
Python 3.12

Все зависимости указываются в requirements.txt

Если потребуется добавить новый формат отчета или вывода, достаточно создать новый класс отчета и зарегистрировать его в REPORTS в main.py

### Пример вывода отчета
1. Таблица
   
![image](https://github.com/user-attachments/assets/c44eeb24-93df-4a6d-81f8-26d647b34c81)

2. JSON
   
 ![image](https://github.com/user-attachments/assets/d18cc0b3-ebc0-41b4-bc16-73e608795245)




