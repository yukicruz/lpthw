from sys import exit

i = 0


# Receive a paycheck from work; display choices
def start_work():
    print("You just worked another two weeks. It's payday.")
    print("Do you want to go out, "
          "go to the bank, or put it under your mattress? ")

    use_money = input("> ")

    if "out" in use_money:
        dead("You spent all your money on booze and loose women.")
    elif "bank" in use_money:
        bank()
    else:
        print("That's boring and uncreative...")
        start_work()


def dead(why):
    print(why, "You're going to work for life! Good job")
    exit(0)


def bank():
    print("Welcome to the bank!")
    print("Would you like to put your money in your savings account or"
          " invest it in a business you'd like to run?")

    use_money = input("> ")

    if "savings" in use_money:
        print("Did you know you lose more money to inflation than"
              " you gain with our interest rate? ")
        input("> ")
        start_work()
    elif "business" or "invest" in use_money:
        business(i)
    else:
        dead("What are you doing?")


def business(i):
    print("You're working on your business today!")
    print("Do you want to work and invest wisely,\n"
          " try to retire,\n"
          " or spend it all?")

    decision = input("> ")

    if i == 3:
        dead("All work and no play makes a boring life.")
    elif "wise" in decision or "invest" in decision or "work" in decision:
        print("Good choice")
        i += 1
        business(i)
    elif "retire" in decision and i == 0:
        print("Too soon...your business went belly up."
              " Try working a little smarter next time."
              " Luckily, you didn't quit your day job!")
        start_work()
    elif "retire" in decision and i > 0:
        print("Congrats! You're living on passive income!")
    else:
        dead("I don't get it.")
        exit(0)


start_work()
