n_list = [1,20,-3,4,-20,10,100]
result = []
for a in filter(lambda x : x < 0, n_list):
    result.append(a)
    

print(result)