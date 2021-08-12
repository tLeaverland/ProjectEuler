ONES = ["", "one", "two", "three", "four", "five", 
"six","seven","eight", "nine", "ten", "eleven", "twelve", 
"thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
"eighteen", "nineteen"]

TENS = ["","","Twenty", "Thirty", "forty", "fifty", "sixty", "seventy", "eighty"
,"ninety"]

def num_to_words(n):
    if 0 <= n < 20:
        return ONES[n]
    if 20 <= n < 100:
        return TENS[int(str(n)[0])] + ONES[n % 10]
    if 100 <= n < 1000:
        if str(n)[len(str(n))-2:len(str(n))] == "00":
            return ONES[int(str(n)[0])] + "hundred"
        else:
            return ONES[int(str(n)[0])] + "hundredand" + ((ONES[int(str(n)[len(str(n))-2:len(str(n))])]) if str(n)[1] == "1" else (TENS[int(str(n)[1])] + ONES[n % 10]))
    else:
        return("onethousand")

print(num_to_words(110))

sum = 0

for i in range(1, 1001):
    sum += len(num_to_words(i))

print(sum)
    



