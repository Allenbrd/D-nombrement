def permute(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        firstElement = lst[i]
        lstRestante = lst[:i] + lst[i+1:]
        for j in permute(lstRestante):
            l.append([firstElement] + j)
    return l

data = list('123456789')
results = []
counter = 0
for res in permute(data):
    counter+=1
    results.append(res)
    
with open('readme.txt', 'w') as f:
        f.write(str(results))
print(counter)
