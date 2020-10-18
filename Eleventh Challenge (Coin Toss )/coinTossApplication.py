import random

print("Welcome to teh Coin Toss App")

# get user input
flip_number = int(input("How many times would you like to flip the coin : "))
choice = input("Would you like to see the result of each flip (y/n): ").lower()

print("\nFlipping\n")

# initialize variables
heads = 0
tails = 0

# The main loop
for flips in range(flip_number):
    coin = random.randint(0, 1)
    if coin == 1:
        heads += 1
        if choice.startswith("y"):
            print("HEADS")
    else:
        tails += 1
        if choice.startswith("y"):
            print("TAILS")
    if heads == tails:
        print(
            "At "
            + str(flips + 1)
            + " flips, the number of heads and tails were equal at "
            + str(heads)
            + " each."
        )


# calcuate percentage

head_percentage = round(100 * heads / flip_number, 2)
tail_percentage = round(100 * tails / flip_number, 2)

# Print the results
print("\nResults of Flipping a Coin " + str(flip_number) + " Times: ")
print("\nSide\t\tCount\t\tPercentage")
print(
    "Heads\t\t"
    + str(heads)
    + "/"
    + str(flip_number)
    + "\t\t"
    + str(head_percentage)
    + "%"
)
print(
    "Tails\t\t"
    + str(tails)
    + "/"
    + str(flip_number)
    + "\t\t"
    + str(tail_percentage)
    + "%"
)

