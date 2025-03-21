
# Use the logging package to write a program to output a specific message from a list of 5 logging levels. The program must accept input in the following format: log number. The log number options are 10, 20, 30, 40, 50.

# The message entries for each level are:

# DEBUG – “10:Debug test”

# INFO – “20:Program successful!”

# WARNING - “30:Warning, there could be errors”

# ERROR - “40:Program encountered an error!”

# CRITICAL – “50:The program has stopped working!”

# For example, when the user enters:

# log 30

# Output should be:

# Warning, there could be errors

def log_message(log_input):
    log_number = log_input[4:6]
    if log_number == str(10):
        print("Debug test\n") 
    elif log_number ==  str(20):
        print("Program successful!\n")
    elif log_number == str(30):
        print("Warning, there could be errors\n")
    elif log_number == str(40):
        print("Program encountered an error!\n") 
    elif log_number == str(50):
        print("The program has stopped working!\n") 
    
if __name__ == '__main__':
    log_input = input()
    log_message(log_input)