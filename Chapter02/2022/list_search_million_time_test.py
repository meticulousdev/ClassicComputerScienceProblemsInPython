import random
import time
from generic_search import linear_contains, binary_contains


# test_fcn = linear_contains # 여기에 hash를 넣을 방법은 없을까?
test_fcn = binary_contains 

Nmax = 10000000
Nsam = 10000000
Ntry = 30
mylist = sorted(random.sample(range(0,Nmax), k=Nsam))

elapsed = [None] * Ntry
result = [None] * Ntry
print('start now')
for i in range(Ntry):
    toFind = random.randint(0, Nmax)
    # print(mylist)
    # print(toFind)

    start = time.time()
    result[i] = test_fcn(mylist, toFind)
    elapsed[i] = time.time()-start

print(f'{sum(elapsed)/len(elapsed):10.8f} sec')

print(elapsed)
print(result)