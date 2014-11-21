import sqlite3


conn = sqlite3.connect("users.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT unique, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)''')


def list_employees():
    all_employees_info = cursor.execute('''SELECT * FROM users''')
    for employee in all_employees_info:
        print("{} - {}".format(employee["name"], employee["position"]))


def monthly_spending():
    result = cursor.execute(
        '''SELECT SUM(monthly_salary) from users''').fetchone()
    print(result[0])


def yearly_spendings():
    result = cursor.execute(
        '''SELECT SUM(monthly_salary) from users''').fetchone()
    print(12 * result[0] * 12)


def add_employee():
    name = input("name: ")
    monthly_salary = input("monthly_salary: ")
    yearly_bonus = input("yearly_bonus: ")
    position = input("position: ")
    cursor.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
                   (name, monthly_salary, yearly_bonus, position))


def delete_employee(employee_id):
    cursor.execute('''DELETE FROM users WHERE id = ?''', (employee_id))


def update_employee(employee_id):
    name = input("name: ")
    monthly_salary = input("monthly_salary: ")
    yearly_bonus = input("yearly_bonus: ")
    position = input("position: ")
    cursor.execute('''UPDATE users SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?''',
                   (name, monthly_salary, yearly_bonus, position, employee_id))


def main():
    command = ""
    while command != "exit":
        command = input("enter command: ")
        command = command.split(" ")
        if command[0] == "list_employees":
            list_employees()
        elif command[0] == "yearly_spendings":
            yearly_spendings()
        elif command[0] == "monthly_spending":
            monthly_spending()
        elif command[0] == "add_employee":
            add_employee()
        elif command[0] == "delete_employee":
            delete_employee(command[1])
        elif command[0] == "update_employee":
            update_employee(command[1])
        elif command[0] == "exit":
            break
        else:
            print("Wrong command!")

    conn.commit()


if __name__ == '__main__':
    main()
