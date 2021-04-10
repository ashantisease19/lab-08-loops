average = 0
sum = 0

for i in range (0,4,1):
    userinput = input("Just give me a number.")
    usernum = int(userinput, 10)
    sum = sum + usernum
    print("So you put the number " + str(usernum) + " and the current sum is " + str(sum))

average = sum / 4
print("Okay, bro, so the average is " + str(average))
