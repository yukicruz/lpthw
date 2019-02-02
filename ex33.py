numbers = []


def loop_i(n):
    i = 0
    while i < n:
        print(f"At the top i is {n}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {n}")

    print("The numbers: ")


print(f"How many times do you want to loop?")
n = int(input("> "))
loop_i(n)

for num in numbers:
    print(num)
