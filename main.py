print("Program starting.")
Number=int(input("Insert a positive integer: "))
steps=0
while Number != 1:
    print(Number, end=" -> ")
    if Number % 2 == 0:
        Number = Number // 2
    else:
        Number = (Number * 3) + 1
    steps += 1
print(Number)
print("Sequence had", steps, "total steps.")
print("\nProgram ending.")