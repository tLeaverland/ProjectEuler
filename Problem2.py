fib_array = [1,2]
even_fib = []
index = 1
while (fib_array[index] + fib_array[index-1]) < 4000000:
  fib_array.append(fib_array[index] + fib_array[index - 1])
  if (fib_array[index] + fib_array[index - 1]) % 2 == 0:
      even_fib.append(fib_array[index] + fib_array[index - 1])
  index += 1  
print(even_fib)
print(sum(even_fib))
