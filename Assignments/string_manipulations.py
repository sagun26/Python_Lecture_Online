'''
Reverse a String: Write a function that takes a string as input and returns the string reversed. 
For example, if the input is "hello", the output should be "olleh".
'''def reverse(a):
    return a[::-1]

str_rev = reverse('hello')
print(str_rev)'''

Count Vowels in a String: Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
For example, if the input is "hello", the output should be 2.
using loop
'''
def string_input(  a):
  count=0;
  for char in a:
    if char.lower()  in ['a', 'e', 'i', 'o', 'u']:
     count +=1 
     return count;
    str_a= "hello"
vowel_count=string_input(str_a)
print(vowel_count)
'''
Check Palindrome: Write a function that checks if a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward. 
For example, "radar" is a palindrome.
#reverse a string
'''
def reverse(a):
    return a[::-1]
b ='radar'
str_rev = reverse(b)
if (str_rev==reverse(b)):
 print("palindrome")
else:
 print("not palindrome")
'''
String Anagrams: Write a function that checks if two strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once. 
For example, "listen" and "silent" are anagrams.


#Optional Try your best
Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating characters in "abcabcbb" is "abc", 
which has a length of 3.
'''
