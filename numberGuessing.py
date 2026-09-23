import random   # for random number guess generator

def random_guess(low, high):    # guesses a random number within the range low-high
    return random.randint(low, high)

# checks if secret num meets requirement
secret = input("input a number between 0 and 50: ")
while not secret.isdigit() or not 0 <= int(secret) <= 50:
    secret = input("input a number between 0 and 50: ")
secret = int(secret)

low = 0
high = 50   # setting initial values for these 2 variables

while low <= high:  # handles rare case where low and high are = to one another but haven't been guessed yet
    guess = random_guess(low, high) # using function above
    answer = input(f"number = {guess}? enter correct, higher, or lower: ")  # user describes correlation to secret number
    while answer not in ("correct", "higher", "lower"):
        print("type correct, higher, or lower") # must be identical to as written here
        answer = input(f"number = {guess}? enter correct, higher, or lower: ")
    if answer == "correct":     # if correct
        print("all done")
        break
    elif answer == "higher":    # if secret is higher
        low = guess + 1
    elif answer == "lower":     # if secret is lower
        high = guess - 1
else:
    print("out of numbers to guess")

# notes: this code doesn't check if the user saying higher or lower is actually being honest in correlation to the guess and secret number

