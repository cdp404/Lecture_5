from functools import reduce

n_list = [10, 20, 30, 40, 50]
print(reduce(lambda x,y:x**2+y, n_list))

