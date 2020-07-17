def adult_func(n):
    if n>=19:
        return True
    else :
        return False

age = int(input('나이입력 : '))
print(adult_func(age))

ages = [33,34,35,36,15,16,17]
for a in filter(adult_func,ages):
    print(a)