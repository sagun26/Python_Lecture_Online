
'''
A datatype storing multiple similar or different data types 
is called collection data type

[1,2,3,4,5]
[1,'2',3.0,4.0,5]
'''
#Data type 1: 
#List 
'''
starts and ends with big brackets
[1,2,3,4]
'''

# list_val=[1,'2',3.0,4.0]
# print(list_val)
# print(type(list_val))

# #Traversing each element
# print(list_val[0]) #Returns first element
# print(list_val[1]) #Returns second element

# print(list_val[-1]) #Last element
# print(list_val[-2]) #2nd last element

# #len() function gives the length of list
# print(f'Length of list is: {len(list_val)}')

# #append to basically add new element at the end
# list_val.append('5.5')
# print(list_val)

# #pop()
# print(list_val.pop())
# print(list_val)

# '''
# list is mutable: Any element can be modified
# '''
# list_val[0]+=1
# print(list_val)

# list_val=[1,2,3,4,5]
# print(list_val)
# list_val[0]=list_val[0]+5
# list_val[1]=list_val[1]*2
# list_val[2]=list_val[2]-1
# print(list_val)

'''
let's create a simple app
which takes 2 inputs 
add the 2 inputs in list 
put the sum of 2 inputs in the list as well
'''
#Take input 1
#Take input 2
# put the 2 elements in list
# sum of 2 elements
# put the result in list

list_of_elements=[]
element_1=int(input('Enter 1st element: '))
element_2=int(input('Enter 2nd element: '))

#Adding elements on list
#Approach 1
# list_of_elements.append(element_1)
# list_of_elements.append(element_2)

#Approach 2: 
list_of_elements=[element_1,element_2]


#Sum of elements in list: 
#Approach 1: 
# sum_of_elements=list_of_elements[0]+list_of_elements[1]
# list_of_elements.append(sum_of_elements)
# print(list_of_elements)

#Approach 2: 
sum_of_elements=sum(list_of_elements)
list_of_elements.append(sum_of_elements)
print(list_of_elements)







