# We've been using built-in functions in Python:

print("Hello")
print(type(5.3))

# We call the print function with the argument "Hello".
# We call the type function with the argument 5.3.

my_list = ['Hamzah', 'Michelle', 'Carsten', 'Khai', 'Aiden',
           'Jack', 'Derek', 'Sunny', 'Matt',
           'Cardelina', 'Daniel', 'JP', 'Gael', 'John', 'Ben', 'Grace']
print(sorted(my_list))


# We call the sorted function with argument my_list.

# Now we can define our own functions!

# Define a custom function using the def keyword,
# a name for the function, e.g., blackjack_hand,
# and parentheses
# and a colon (:).
def blackjack_hand():
    # The indented body of the function goes here.
    player_hand = 20
    dealer_hand = 19
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")


# To run the function, we call the function:
# blackjack_hand()

print()


def prompt_for_name():
    name = input("What's your name? ")
    print(f"Hello, {name}.")


# To run the function, we call the function:
# prompt_for_name()


def while_with_flag():
    # Use a flag in a while loop.
    prompt = "\nTell me something, and I'll "
    prompt += "repeat it back to you."
    prompt += "\nEnter 'quit' to end the program. "
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)


# while_with_flag()

# A function can have a changeable part
# called a parameter.
# Give the parameter a **NAME** in the function definition.
# Put it in the parentheses.
def blackjack_hand2(player_hand):
    # The indented body of the function goes here.
    dealer_hand = 19
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")


# Give the parameter a VALUE in the function call.
blackjack_hand2(-10)
blackjack_hand2(21)

print()


# The parameter value is an argument.
# We called blackjack_hand2 with an argument of 21.

def greeting(name):
    print(f'Hello, {name}!')


greeting('Grace')

print()


def cheer():
    for i in range(3):
        print("Go Bears!")


cheer()

print()


def cheer2(team):
    for i in range(3):
        print(f'Go, {team}!')


# Cooperating functions

# I can call a function from inside another function.

def main():
    cheer2('Bears')
    print()
    cheer2('Celtics')
    print()
    cheer2('Sox')
    print()


# main()


# We've seen functions with zero parameters
# and one parameter.

# We can write functions with more than one parameter.

# The function definition includes the parameter NAMES in
# the parentheses.
def blackjack_hand3(player_hand, dealer_hand):
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")


# The function CALL includes the parameter VALUES
# in the parentheses.
blackjack_hand3(19, 7)

# When you use positional arguments as above,
# Python matches the first argument in the function
# call 19 with the first parameter in the function
# definition player_hand.
# Python matches the second argument in the function
# call 7 with the second parameter in the function
# definition dealer_hand.

print()


def cheer3(team, times):
    for i in range(times):
        print(f'Go, {team}!')


# cheer3('Bruins', 3)

# print()

# cheer3('Pats', 5)
def main():
    for i in range(3):
        print('Go Bruins!')
    print()
    for i in range(3):
        print('Go Celtics!')
    print()
    for i in range(3):
        print('Go Sox!')


# main()

def print_models(unprinted, printed):
    '''3d print a set of models.'''
    while unprinted:
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
        printed.append(current_model)
    print(f'We still need to print: {unprinted}')
    print(f'We printed: {printed}')


print_models(['phone case', 'pendant', 'ring'], [])

list1 = ['phone case', 'pendant', 'ring']
list2 = []

print()

# list1 has elements, so if list1 means if True.
if list1:
    print('Yes!')

# list2 has no elements, so if list2 means if False.
if list2:
    print('Yes')


def print_models2(unprinted, printed):
    '''3d print a set of models.'''
    while unprinted:
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
        printed.append(current_model)
    return printed


print()

print(f"The list of printed models is:"
      f" {print_models2(['phone case', 'pendant', 'ring'], [])}")
