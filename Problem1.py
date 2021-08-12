num_array = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        num_array.append(i)

print(sum(num_array))