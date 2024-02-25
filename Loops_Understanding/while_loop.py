'''
when do we use while loop:
whenever a loop is not precise enough 

Let's create a simple game
where we generate random number 
add user input number to that random number 
if new random number is 6 or 12 
end the game else
continue
'''
import random
#print(random.randrange(0,12))

'''
while True:
    random_number=random.randrange(0,12)
    print(f'random number generated {random_number}')
    addition_number=int(input('Enter any number to add: '))
    random_number=random_number+addition_number
    if random_number==6:
        print('Game won !!')
        break # This command basically ends the loop wherever it is encountered.


'''
'''
z=random.randrange(1,10)
print(f'check if any number if multiple of {z}')

while True:
    variable_something=int(input('Enter any number: '))
    # check if the variable is even, if even terminate else continue
    if variable_something%z==0:
        print(f'{variable_something} is multiple of {z}')
        break

'''

while True:
    user_input=input('>>').lower()
    #Make changes here! 
    if user_input=='hello':
        print(user_input)
    elif user_input=='how are you ?':
        print('I am fine')
    elif user_input=='bye':
        break
    else:
        print('Enter valid argument!!')


