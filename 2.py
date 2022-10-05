numbers = [1,3,45,23,66,101,582]
x_min = min(numbers)
x_max = max(numbers)
results = []
for i in numbers:
    if i % 2 == 0:
       results.append(i*x_min)
    else: 
        results.append(i*x_max)
print(results)