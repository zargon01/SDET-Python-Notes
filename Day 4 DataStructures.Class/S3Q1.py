class WorkerDetail:
    def __init__(self, employee_code, name, basic_salary):
        self.employee_code = employee_code
        self.name = name
        self.basic_salary = basic_salary

    def display_method(self):
        print(f"Employee code:{self.employee_code}")
        print(f"Employee name:{self.name}")
        print(f"Employee Basic salary:{self.basic_salary}")

    def calculate_hra(self):
        hra = 0.6 * self.basic_salary
        print(f"HRA:{hra:.1f}")


class OfficerSal(WorkerDetail):
    def calculate_da(self):
        da = self.basic_salary * 0.98
        print(f"DA:{da:.1f}")

class ManagerSal(OfficerSal):
    def calculate_ca(self):
        ca = 0.2 *self.basic_salary
        print(f"CA:{ca:.1f}")

def main():
    employee_code = input()
    name = input()
    basic_salary = float(input())

    obj = ManagerSal(employee_code, name, basic_salary)

    obj.display_method()
    obj.calculate_hra()
    obj.calculate_da()
    obj.calculate_ca()


if __name__ == "__main__":
    main()