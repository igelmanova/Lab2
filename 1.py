words = ["orange", "apple", "banana", "strawberry", "pineapple"]
my_list = []
for i in words: 
    my_list.append(len(i))
result = max(my_list) + min(my_list)
print(result)
