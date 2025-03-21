
# Write a program that will take as input a string of cities along with their city identification numbers. The city ID, City name pair will be comma separated.

# Your program should process these cities into a hash table (with 10 slots) using the simple hash function with chaining for handling collision.

# Note that there should be a single white space at the end of each line, whether it ends with a number or a city name.

# For example, if input is:

# 10 Cincinnati,11 Chicago,12 Boston,20 SouthBend,45 Florence

# The output would be:

# 0 Cincinnati SouthBend 

# 1 Chicago 

# 2 Boston 

# 3 

# 4 

# 5 Florence 

# 6 

# 7 

# 8 

# 9  

def cities_hash_table(str_cities):
    city_array = str_cities.split(",")
    for num in range(0, 10):
        conc_str = f"{str(num)} "
        for i in city_array:
            if i[1:2] == str(num):
                city_name = i[3:]
                conc_str = conc_str + f"{city_name} "
        print(conc_str)
if __name__ == '__main__':
    str_cities = input()
    cities_hash_table(str_cities)