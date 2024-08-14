
#veradarcnel ashakertneri mijin gnahatakany
from function1 import max_school
def average1(args):
    summa = 0
    for i in args:
        summa += i
    mijin = summa // len(args)
    return mijin


def get_average_students_rate(kwargs):
    for key, val in kwargs.items():
        print(key,average1(val))
    return kwargs

result = get_average_students_rate

a = ({
    'gyumri': [1,2,3],
    'erevan': [1, 8, 10, 9],
    'lori': [9, 8, 10, 21],
})
get_average_students_rate(a)
print("haxtec :",max_school(a))






# test apa login exni credential.yml-i tvyalnerov ete che apa unique tvyalnerov

# edf login():
