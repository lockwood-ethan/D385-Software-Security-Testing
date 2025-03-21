
# Write a program that will accept four grades and place them in a list. The sum of the 4 grades should be less or equal to 100. Each individual grade should be greater or equal to 0, but less or equal to 100. Include an assert statement that will display a message if any of these conditions are not met. The assert statements should display the messages "All values need to be greater than 0 but less than 100" and "One of the grades is wrong, total needs to be less than 100!", as appropriate.

# Ex: If the input of the program is:

# 25, 10, 15, 25

# the output of the program is:

# 75

# Ex: If the input of the program is:

# 25, 30, 20, 40

# the output of the program is:

# One of the grades is wrong, total needs to be less than 100!

# Ex: If the input of the program is:

# 25, 30, -1, 40

# the output of the program is:

# All values need to be greater than 0 but less than 100

def test_list(list_of_integers):
    for i in list_of_integers:
        if i >= 0 and i <=100:
            pass
        else: 
            return "All values need to be greater than 0 but less than 100"
    if sum(list_of_integers) >= 0:
        pass
    else: 
        return "All values need to be greater than 0 but less than 100"
    if sum(list_of_integers) <= 100:
        pass
    else: 
        return "One of the grades is wrong, total needs to be less than 100!"
    return sum(list_of_integers)

if __name__ == '__main__':
    user_input = input()
    list_of_strings = user_input.split(", ")
    list_of_integers = [int(x) for x in list_of_strings]
    print(test_list(list_of_integers))