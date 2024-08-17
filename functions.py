

from function1 import max_school
def average1(args):
    summa = 0
    for i in args:
        summa += i
    mijin = summa // len(args)
    return mijin


def get_average_students_rate(kwargs):
    lis_sc = []
    for key, val in kwargs.items():
        avg = average1(val)
        lis_sc.append((key, avg))
    return lis_sc
a = {
    'gyumri': [1,2,3],
    'erevan': [1, 8, 10, 9],
    'lori': [9, 8, 10, 21]
}
result = get_average_students_rate(a)
for i in result:
    print(str(i))

max_school(result)

