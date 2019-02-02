"""
I'm writing this script for practice.
I'm going to write a script to input a number 'n', then
loop and print that number n times.
"""

i = 0
n = int(input("How many times do you want to loop? "))


def loop_n_times(i, n):
    while i < n:
        if i == 0:
            print(f"'i' = 0!\n")
        elif i % 2 == 1:
            print(f"'i' = {i}")
            print("'i' is odd!\n")
        elif i % 2 == 0:
            print(f"'i' = {i}")
            print(f"'i' is even!\n")
        else:
            print("What's going on??")
        # print(i)
        i += 1


loop_n_times(i, n)
