
class Employer:

    def __init__(self, eml_name, eml_role, eml_salary):
        self.name = eml_name
        self.role = eml_role
        self.salary = eml_salary

        print(f'Employer created: name: {self.name}, role: {self.role}, salary: {self.salary}')


if __name__ == "__main__":
    empl = Employer("John McClane", "Police Officer", 43)
