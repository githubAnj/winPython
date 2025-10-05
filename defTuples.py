#get emplyee of the year based on working hours
def employee_check(work_hours):
    employee_of_month = ''
    current_max = 0
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)
work_hours = [('Sam',100), ('Riya',200),('Ram',150),('Jaya',180)]
# result = employee_check(work_hours)
# print(result)
name,hours = employee_check(work_hours)
print(name,hours)
print("\n")
#output: for
# result = employee_check(work_hours)
# ('Riya', 200)
# 
#output: for 
# name,hours = employee_check(work_hours)
# print(name,hours)
# Riya 200
#
