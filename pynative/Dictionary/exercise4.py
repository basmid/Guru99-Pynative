

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

#{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

new_dict = dict.fromkeys(employees, defaults)
print(new_dict)





