n_list = list(range(1,100))

#짝수만 제곱하여 배열 만들기
squre_arr = [x**2 for x in n_list if x%2 ==0]

print(squre_arr)
print("")

squre_arr_2 = [x**2 for x in n_list if (x%2 == 0 and x%3 == 0)]

print(squre_arr_2)