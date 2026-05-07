x = 0

while x > 10:
    y = input("Enter the number you want:")
    y = int(y)
    if y > x:
        print("y is greater than x")
    else:
        print("nothing is greater than x")

    x = x + 1
    