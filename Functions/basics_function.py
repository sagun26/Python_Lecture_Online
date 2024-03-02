'''
In mathematics
    y=f(x)
    x= input of a function 
    y= output of a function

    int function_name(int1,int2)
    {
        return int1+int2;
    }

#1 function definition: 
    defining function and its actions
#2 function call:
    calling that specific function

'''
#print(a+b)
#range(0,10)

#No return type functions
#Function def inition: 
# def name_of_function (arguments/parameters)
def sum_of_2_numbers(a,b):
    print(a+b)

#Function call

#sum_of_2_numbers(1,2)

'''
create a function named calculations
calculations arguments= a,b, flag 
if flag=1, a+b, flag=2 a-b flag=other then 1 and 2 print cant perform random 
operation
'''
'''
#Simran Tamang's Code
def calculations(a,b,flag)
   if(flag == 1):
        print(a + b)
    elif(flag == 2):
        print(a - b)
    else:
        print("Cant perform random operation")

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
flag = int(input("Enter 1 for add and 2 for subtarction: "))
calculations(a, b, flag)
'''
#Anu Sapkota's Code 
def calculations(a, b, flag):
  if (flag==1):
    print(f'Sum: {a+b}')
  elif (flag==2):
    print(f'Difference: {a-b}')
  else:
    print('Cant perform random operation')

# x=int(input('Enter first number: '))
# y=int(input('Enter second number: '))
# z=int(input('Enter flag: '))
# calculations(x, y, z)
    

#Return cases:
'''
y=f(x) f(x),
int main()
{
    return 0;
}

'''
#sum of  2 numbers but this time return results to the main program

def sum_of_2_numbers(a,b):
  #sum=a+b
  #return sum
  return a+b

# addition works as y in the case of y=f(x), so it gets the value a+b
addition=sum_of_2_numbers(1,2)
#print(a+b)

'''
take input from user, 
convert that string to integer by creating a function convert_to_integer
then add the 2 numbers passing to another function named addition_of_2_numbers

convert_to_integer(any)-> int
addition_of_2_numbers(int,int)-> None (Prints output inside the function only)

'''
'''
def convert_to_integer(a):
  return int(a)

def addition_of_2_numbers(a,b):
  print(a+b)

'''


# x=convert_to_integer(input('Enter first number: '))
# y=convert_to_integer(input('Enter Second number: '))
# addition_of_2_numbers(x,y)

'''
#Shraddha Pahari's Code
def addition_of_2_numbers(a,b):
    sum=a+b
    print(f"Addition of {a} and {b} is {sum}")

def convert_to_integer(a,b):
    a=int(a)
    b=int(b)
    addition_of_2_numbers(a,b)


a=input("Enter the first number:")
b=input("Enter the second number:")
convert_to_integer(a,b)
'''



#Nested Function:
'''
g(x)=h(y)
z=g(y)
function within a function
#define funtion first 
def addition_of_2_numbers(a,b):
    #Nested Function Definition
    def another_function(c):
        return int(c)
    #Nested Function Call
    another_function()
    print(a+b)
#then call function
addition_of_2_numbers(1,2)
    
addition_of_2_numbers(a,b)
{
    convert_to_integer(x)
    {
        return int(x)
    }
    a=convert_to_integer(a)
    b=convert_to_integer(b)
    print(a+b)
}
convert this pseudo code into python code 
convert_to_integer(any) -> integer type
addition_of_2_numbers(any,any) -> None (displays sum of 2 numbers )
'''
#Parent Function definition
def addition_of_2_numbers(a,b):
  
  #Nested Child Function Definition
  def convert_to_integer(x):
    return int(x)
 
  #Nested Child Function Call
  a=convert_to_integer(a)
  b=convert_to_integer(b)
  print(a+b)

a1=input('Enter first number: ')
#Understanding the scope of convert_to_integer()
#a1=convert_to_integer(a1)

a2=input('Enter second number: ')
addition_of_2_numbers(a1,a2)


'''
learn about lamda functions
learn about args and kwargs,
learn about default arguemnts setup
'''



