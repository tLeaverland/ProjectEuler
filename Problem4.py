def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

palindromes = []

for i in range(999):
    for j in range(999):
        num = i * j
        if is_palindrome(num):
            palindromes.append(num)

print(max(palindromes))