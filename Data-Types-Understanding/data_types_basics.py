
# understanding the basics of datatypes

'''
integer
float
double
character
string
[array]

int variable_name;
a=4
'''
#Starting of code snippet here. Start with basics
# a is a variable containing data types integer, float and string
'''
a=4
print(type(a))

a=4.0
print(type(a))

a='4.0'
print(type(a))

a=4
b=5.0
print(a+b)
'''

#Code snipet to understand how to take input and convert the datatypes
'''
#Approach 2
#converting the input as soon as we recieve it
input_1=int(input('Enter any number: '))
input_2=int(input('Enter any number: '))

#Approach 1
#Converting to integer and returning it on variables
input_1=int(input_1)
input_2=int(input_2)

#Approach 3
#Converting the variables at the very last operation to get required results.
print(int(input_1)+int(input_2))

'''

#Few operations in python
'''
Arthimatic Operation: 
    + sum (a + b)
    - difference (a - b )
    * multiplication (a * b)
    / division (a / b )
    % modulus ( a % b )

increment decrement operation:
    a++ substitute a+=1 if u want to increase by 2 vaney a+=2
    a-- substitute a-=1


Comparison operation: 
    a>b -> True , False    
'''


#input('Enter xyz ') -> int(string) -> integer

#let's build a calculator: 
'''

Take 2 numbers from user, 
Display Sum of 2 numbers, difference of 2 numbers, division of 2 numbers (quotent and remainder) and multiplication of 2 numbers

'''


a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))

print(a,b)

#Terrible way of display 
#print('sum of 2 numbers: ')
#print(a+b)

#Better way of display 
#Approach 1: 
# print('sum of 2 numbers approach 1: '+str(a+b))

#Approach 2: (formatted string)
print(f'sum of 2 numbers: {a+b}')
print(f'Difference of 2 numbers: {a-b}')
print(f'division of 2 numbers (quotent): {a/b}')
print(f'Divison of 2 numbers (Remainder): {a%b}')
print(f'Multiplication of 2 numbers: {a*b}')
print(f'Is a greater then b: {a>b}')

