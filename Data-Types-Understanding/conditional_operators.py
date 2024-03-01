'''
if (condition):
    condition_true
else:
    condition_false

'''
'''
a_number=2 #Take it from user
a_number=int(input('Enter any number: '))

if a_number%2==0:
    print(f'{a_number} is even')
else:
    print(f'{a_number} is odd')
'''

'''
Let's make a calculator where 
person enters 1st number
person enters 2nd number
person enters operator symbol: 
    + = sum
    - = difference 
    / = quotent
    % = reminder
    * = multiplication
'''

'''
first_number=int(input('Enter 1st number: '))
second_number=int(input('Enter 2nd number: '))
operators=input('Enter operator to use: ')

# == check if equal     = assign value
# === ???

if operators=='+':
    print(f'sum of 2 numbers: {first_number+second_number}')
elif operators=='*':
    print(f'product of 2 numbers: {first_number*second_number}')

'''

'''
Assignment try it out using match and switch as well 
if not possible please give your reasonings.
'''
#match and switch
user_input  = str(input("Enter your gender: ")).lower()

match user_input:
    case "male":
        print("User is male")
    case "female":
        print("User is female")
    case _:
        print("User is other gender") 

'''
Take 2 input from user, 
compare the 2 variables
print the greater variable
'''
var_1=int(input('Enter 1st variable: '))
var_2=int(input('Enter 2nd variable: '))

if (var_1>var_2)==True:
    print(f'Greater number is {var_1}')
else:
    print(f'Greater number is {var_2}')






