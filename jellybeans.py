guess = ["256", "8", "Alan", "240", "Betty", "232", "Cheng", "253", "Dimitri", "284", "Evan", "300", "Fathima", "258", "Gurtrude", "206", "Harry", "238"]
amount = int(guess[0])
loop = int(guess[1])

num = 3
least = 0 
point = 0

for i in range (loop-1):
    x = abs(amount-int(guess[num]))
    if i == 0:
        least = x
    if x < least:
        least = x
        point = num
    num += 2

print(guess[point-1])
