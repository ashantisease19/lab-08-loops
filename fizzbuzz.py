# for(var i= 1; i <= 100; i=)
for i in range(1,100,1):
    if(i % 3 == 0 and i % 5 == 0):
        print("Fizzbuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
