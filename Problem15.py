limit = 1000000

def collatz_length(n):

    lengths = {}

    for i in range(1, n):

        start = collatz = i
        count = 0

        while collatz != 1:
            if collatz in lengths:
                count += lengths.get(collatz) + 1
                collatz = 1
                break
            if collatz % 2 == 0: 
                collatz /= 2
            else:
                collatz = 3*collatz + 1
            count += 1

        lengths[start] = count
    return lengths

max_collatz = max(collatz_length(limit), key = collatz_length(limit).get)

print("The longest collatz sequence corresponds to ... n = {}".format(max_collatz))