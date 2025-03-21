
# Write a program that will take as input, an index to the list [5, 10, 15, 20, 25]. The program should then print the element referenced by the entered index along with the elements that come immediately before and after. Use exception handling to handle out of index references. The program should notify the user when such an exception occurs.

# Ex: If the input of the program is:

# 0

# the output of the program is:

# One of the elements is out of bounds

# Ex: If the input of the program is:

# 1

# the output of the program is:

# 5 10 15

# Ex: If the input of the program is:

# 4

# the output of the program is:

# One of the elements is out of bounds

def print_num(user_input):
    user_input = int(user_input)
    num_list = [int(5), int(10), int(15), int(20), int(25)]
    if user_input < 0 or user_input >4:
        return "One of the elements is out of bounds"
    else:
        pass
    before = user_input - 1
    if before < 0:
        return "One of the elements is out of bounds"
    else:
        pass
    after = user_input + 1
    if after > 4:
        return "One of the elements is out of bounds"
    else:
        pass
    result = f"{num_list[before]} {num_list[user_input]} {num_list[after]}"
    return result

if __name__ == '__main__':
    print(print_num(input()))