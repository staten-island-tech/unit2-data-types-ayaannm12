def gcf(x ,y):
    if x < y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller + 1):
     if x % i == 0 and y % i == 0:
        gcf = i
    return(gcf)
number1 = 27
number2 = 9
print("gcf of ", number1, "and", number2, "is", gcf(number1, number2))