#Header----------------------------------------------------

#Name: Paul_Array
#Programmer: Paul Muresan
#Date Finished:
#Description: Allows user to enter a mathematical expresion,
#then ask for a split size and then organize into lists.

#Checking Functions-----------------------------------------

#Checking for a negative function

def negative_check(x):

    for i in range(len(x)): #Loop to check every location
        if x[i] == "-":
            return True
        else:
            return False

#Checking for a decimal function
def decimal_check(x):

    for i in range(len(x)): #Loop to check every location
        if x[i] == ".":
            return True
        else:
            return False

#Checking for even number
def even_check(x):

    x = str(x/2)

    if decimal_check(x) == True:
        return False
    elif decimal_check(x) == False:
        return True

#Output Functions-------------------------------------------

def find_unique_operators(x):   #Finding unique operators

    unique_operator_list = []
    has_plus = False
    has_minus = False
    has_multiply = False
    has_divide = False

    for i in range(len(x)): #Loop to check each location for +
        if x[i] == "+":
            has_plus = True
    
    for i in range(len(x)): #Loop to check each location for -
        if x[i] == "-":
            has_minus = True

    for i in range(len(x)): #Loop to check each location for *
        if x[i] == "*":
            has_multiply = True

    for i in range(len(x)): #Loop to check each location for /
        if x[i] == "/":
            has_divide = True

    #Creating list of unique operators
    if has_plus == True:
        unique_operator_list.append("+")
    if has_minus == True:
        unique_operator_list.append("-")
    if has_multiply == True:
        unique_operator_list.append("*")
    if has_divide == True:
        unique_operator_list.append("/")

    x = unique_operator_list

    #Return
    return x 

def first_n(n,l):   #Finding first n

    n = int(n)
    print(l[0:(n+1)])

def last_n(n,l):    #Finding last n

    n = int(n)
    print(l[n:(len(l))])

def middle_n(n,l):  #Finding middle n

    n = int(n)  #Ensuring n is an int

    if even_check(n) == False:  

        mid_index = int((round(len(l) / 2)) - 1)
        start_call = int((mid_index) - (n/2))
        end_call = int((start_call) + n)

    elif even_check(n) == True:

        mid_index = int(round(len(l) / 2))
        start_call = int((mid_index) - (n/2))
        end_call = int((start_call) + n)

    print(l[start_call:end_call])

def find_median(l): #Finding the median and numbers greater than it

    median = 0
    total = 0

    for i in range(len(l)):
        median = median + int(l[i])

    median = round(median / int(len(l)))

    for i in range(len(l)):
        if int(l[i]) >= median:
            
            total = round(total + int(l[i]),2)
    
    return total

def read_expression(l):

    expression = []
    total_string = ""
    total = 0

    #Sorting each individual character into a list
    for i in range(len(l)):
        expression.append(l[i])

    print("The expression is ", expression)

    #Replacing the comma with the first operator
    for i in range(len(expression)):
        if expression[i] == ",":
            expression.insert(expression[0],expression[i])
            del expression[0]

    #Turning each character into a string and adding it to a greater string
    for i in range(len(expression)):
        total_string = total_string + str(expression[i])

    for i in range(len(total_string)):

        if total_string[i].isdigit:

            #Calculation of the first two integers
            if i == 1 and total_string[i+1] == "+":
                total = int(total) + int(total_string[1]) + int(total_string[3])
            elif i == 1 and total_string[i+1] == "-":
                total = int(total) + int(total_string[1]) - int(total_string[3])
            elif i == 1 and total_string[i+1] == "*":
                total = int(total) + int(total_string[1]) * int(total_string[3])
            elif i == 1 and total_string[i+1] == "/":
                total = int(total) + int(total_string[1]) / int(total_string[3])

            #Other calculations
            if (i < len(total_string) - 2) and i != 1 and total_string[i+1] == "+":
                total = int(total) + int(total_string[i+2])
            elif (i < len(total_string) - 2) and i != 1 and total_string[i+1] == "-":
                total = int(total) - int(total_string[i+2])
            elif (i < len(total_string) - 2) and i != 1 and total_string[i+1] == "*":
                total = int(total) * int(total_string[i+2])
            elif (i < len(total_string) - 2) and i != 1 and total_string[i+1] == "/":
                total = int(total) / int(total_string[i+2])

    print("The total of the expression is ", total)


    

#Main-------------------------------------------------------

def main():

    #Variables
    unique_operators = []
    inputted_integer = ""   
    input_integers = [] #List of integers
    inputted_operator = ""
    input_operators = [] #List of operators
    end_input = False
    n = ''
    n_loop = False
    above_median = []
    additional_start = False
    additional_start_loop = True
    assignment_input_file = "assignment_input.txt"
    input_file = open(assignment_input_file, "r")
    line_read = input_file.read()
    line_read = line_read.strip("\n")
    reading_input = []
    reading_variable = ""

    #Main Loop
    while (end_input == False):

        inputted_integer = input("Enter an integer: ") #Integer input

        if decimal_check(inputted_integer) == True: #Checking for decimal

            print("\n!!! INVALID INPUT !!!\n") 
        
        elif decimal_check(inputted_integer) == False and negative_check(inputted_integer) == True: #Checking for negative
            
            if inputted_integer[1].isdigit: #Validating that an integer was inputted

                inputted_operator = input("Enter an opterator (+,-,* or /): ")  #Operator input

                if (inputted_operator == "+" or inputted_operator == "-"    #Validating the operator
                or inputted_operator == "*" 
                or inputted_operator == "/"):

                    #Appending of inputs
                    input_integers.append(inputted_integer)
                    input_operators.append(inputted_operator)  

                elif inputted_operator == "=":  #End loop

                    input_integers.append(inputted_integer)
                    end_input = True
                else:
                    print("\n!!! INVALID INPUT !!!\n") 

        else:  #Negative not found

            inputted_operator = input("Enter an opterator (+,-,* or /): ")  #Operator input
        
            if (inputted_operator == "+" or inputted_operator == "-" #Operator validation
                or inputted_operator == "*" 
                or inputted_operator == "/"):

                #Appending inputs
                input_integers.append(inputted_integer)
                input_operators.append(inputted_operator)  

            elif inputted_operator == "=":  #End loop

                input_integers.append(inputted_integer)
                end_input = True
            else:
                print("\n!!! INVALID INPUT !!!\n")  

    #Outputs---------------------

    #Output 1 and 2
    print("The integers are ", input_integers)   
    print("The operators are ", input_operators)  

    #Output 3
    unique_operators = find_unique_operators(input_operators)
    print("The unique operators are ", unique_operators)

    #Output 4

    if end_input == True:   #Only activate n loop after integers and operators are entered
        n_loop = True

    #n value input
    while n_loop == True:
        n = input("\nInput an n value: ")

        #Validating n
        if negative_check(n) == False and decimal_check(n) == False and int(n) < int(len(input_integers)) and int(n) > 0:

            print("\nn is valid\n")

            #Outputs with n
            print("First n")
            first_n(n,input_integers)
            print("Last n")
            last_n(n,input_integers)
            print("Middle n")
            middle_n(n,input_integers)

            n_loop = False
        else:
            print("\n!!! INVALID INPUT !!!\n")
    
    #Output 5

    #Assigning the integer list to the variable used in the function
    above_median = input_integers   
    above_median = find_median(above_median)

    print("The total of all integers greater than or equal to the median is ", str(above_median))    

#Additional Section-----------------------------------------

    while additional_start_loop == True:

        #Start additional program question
        additional_start = input("Would you like to continue? Enter O for yes or X for no or quit to close program\n")

        if additional_start == "O": #Agreed to start second part

            print("\nOk sweet\n")
            additional_start_loop = False
        elif additional_start == "X":   #Did not agree to start second part

            print("\nOh... ok...\n")
        elif additional_start == "quit":    #Chose to close program
            additional_start = False
        else:   #Invalid input
            print("\nBro that's an invalid input, it's an o not a zero\n")
    
    while line_read != "": #validation for empty strings

        reading_variable = line_read
        reading_input.append(reading_variable)
        read_expression(reading_input)
        line_read = input_file.read()
    input_file.close()



#Main Call--------------------------------------------------

main()
        

