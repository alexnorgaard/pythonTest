import copy


class Employee:
    def __init__(self, name, skillset):
        self.name = name
        self.skillset = skillset

    def add_skill(self, skill):
        self.skillset.append(skill)

    def remove_skill(self, skill):
        self.skillset.remove(skill)


class Continue(Exception):
    pass


employees = []

employees.append(Employee('A', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))
employees.append(Employee('B', ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k']))
employees.append(Employee('C', ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']))
employees.append(Employee('D', ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']))
employees.append(Employee('E', ['n', 'o', 'p', 'q', 'r', 's', 't', 'u']))
employees.append(Employee('F', ['a', 'b', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']))
employees.append(Employee('G', ['a', 'e', 'i', 'o', 'u', 'y']))
employees.append(Employee('H', ['b', 'c', 'e', 'g', 'k', 'm', 'q', 's', 'x']))

combination_list = []
final_combination_list = []


def combine_skills(needed_skills, combination, employees_list):

    for employee in employees_list:
        # print(employee.name)
        temp_combination = copy.copy(combination)
        temp_employees = copy.copy(employees_list)
        temp_needed_skills = copy.copy(needed_skills)

        for skill in employee.skillset:
            if skill in temp_needed_skills:
                temp_needed_skills.remove(skill)

                if employee.name not in temp_combination:
                    temp_combination.append(employee.name)

        temp_employees.remove(employee)
        if not temp_needed_skills:
            if temp_combination in combination_list:
                continue
            combination_list.append(temp_combination)
        else:
            combine_skills(temp_needed_skills, temp_combination, temp_employees)


def post_process():
    for combination in combination_list:
        try:
            for combination1 in combination_list:
                if combination is combination1:
                    continue
                elif all(name in combination for name in combination1) and len(combination1) is len(combination):
                    combination_list[combination_list.index(combination)] = []
                    raise Continue
                elif combination and combination1 and all(name in combination for name in combination1) and len(combination1) < len(combination):
                    combination_list[combination_list.index(combination)] = []
                    raise Continue

        except Continue:
            # print(combination_list)
            continue

    for combination in combination_list:
        if not combination:
            continue
        else:
            final_combination_list.append(combination)


def print_combos():
    for combination in final_combination_list:
        print(combination)


string_skills = input('Write skill combination separated by commas - E.g a,b,c: ').split(',')

combine_skills(string_skills, combination=[], employees_list=employees)
post_process()
print_combos()
