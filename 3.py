from random import uniform

n, n_min, n_max = map(int, input().split()) 
lst_random = []
for _ in range(n):
    lst_random.append(uniform(-10, 10))
counter = 0
for i in lst_random:
    if i >= n_min and i <= n_max:
        counter += 1
print(counter)