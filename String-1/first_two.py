#!/usr/bin/python3
# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
  if len(str) < 2:
    return(str)
  else:
    return str[:2]

print(first_two('a'))
print(first_two('Kitten'))
print(first_two('hiya'))
print(first_two('abcdefg'))