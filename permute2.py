min = 123456789
max = 987654321

def check_duplicate(l):
    mySet = set(l)
    if len(mySet) == len(l):
        return False
    else:
        return True

count = 0

for i in range (min, max+1):
    if '0' not in str(i):
        if check_duplicate(list(str(i))) != True:
            count+=1
print(count)
