# def summa(a,b):
#     return a +b
#
# result = summa(5,7)
#
# def umnojenie(a,b):
#     return (a*b)
#
# print(umnojenie(result,2))

import yaml
def login():
    with open("credentials.yml.", 'r') as f:
        v = yaml.safe_load(f)


