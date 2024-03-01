'''
while loop is used whenever we don't know the precise place to stop
for (c=0,c<10,c++)
{
    some code here
}
#including 0 and excluding 10 
[0,10)

'''
#Basic understanding of for loop and while loop
'''
print('From For Loop')
for var_loop in range(0,10,1):
    print(var_loop)

print('From While Loop')
var_loop=0
while True:
    print(var_loop)
    var_loop+=1
    if var_loop==10:
        break

'''
# Display all even numbers from 1-100 using for loop and also while loop

#While loop first
'''
var_loop=1
while True:
    if var_loop%2==0:
        print(var_loop)
    else:
        pass

    var_loop+=1
    if var_loop==101:
        break

'''
    
#For Loop second
'''
for var_loop in range(2,101,2):
    print(var_loop)

'''

'''
empty_list=[]
empty_list.append(1)
print(empty_list)
'''
#Put all the even numbers in a list named even and odd numbers in list named odd, display both list

odd_list=[]
even_list=[]

for num in range(1,101,1):
    if num%2==0:
        #even
        even_list.append(num)
    else:
        #odd
        odd_list.append(num)
    

# print(f'odd list: {odd_list}')
# print(f'even_list: {even_list}')

'''
list_val=[1,2,3]
for element in list_val
    in first iteartion element=list_val[0]
    in second iteration element= list_val[1]
    in third iteration element=list_val[2]

'''

'''
for list_variable in even_list:
    print(list_variable*100)
'''

#In even list display multiples of 4 and 6
'''
print('Multiple of 4 and 6')

for list_variable in even_list:
    if (list_variable%4==0) and (list_variable%6==0):
        print(list_variable)
    #standard approach
    else:
        pass


# In odd list display multiples of 3 or 27
for list_variable in odd_list:
    if(list_variable%3==0) or (list_variable%27==0):
        print(list_variable)

'''
# Take nth term from user, display fibonacci numbers till nth term 

first_number=0
second_number=1

nth_term=int(input('Enter nth term: '))

print(first_number)
print(second_number)
for count in range(3,nth_term+1,1):
    first_number=first_number+second_number
    print(first_number)
    t_num=second_number
    second_number=first_number
    first_number=t_num

'''
simran's solution: 

user_input = int(input("Enter nth term: "))
first_num = 0
second_num = 1i += 1
print(first_num )
print(second_num)
for cout in range (2, user_input, 1):
    sum = first_num + second_num
    print(sum)
    first_num = second_num
    second_num = sum

'''

'''
Asmita Paudel's Solution: 

Fibonacci = []
n = int(input("Enter nth term: "))
a, b = 0, 1
for _ in range(n):
    Fibonacci.append(a)
    a, b = b, a + b
print(Fibonacci)
'''

'''
#Shraddha Pahari's Solution: 
i = 0
while (i <= nth_term):
    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number
    print(next_number)
    i += 1
'''
'''
#Aarati Subedi's Solution: 
count=0
first_number=0
second_number=1
nth_term=int(input('enter the nth term: '))
# for count in range(2 ,nth_term+1,1):
#     first_number=first_number+second_number
#     print(first_number)
while(count<nth_term):
    print(first_number)
    result=first_number+second_number
    first_number=second_number
    second_number=result
    count+=1
'''
