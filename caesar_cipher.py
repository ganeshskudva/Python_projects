import sys

string = raw_input("Enter plain text str:") 
key = input("Enter key for Caesar Cipher:")
str_list = []

if (key > 256):
    key = key % 256

for c in string:
       str_list.append(chr(ord(c) + key))

print ''.join(str_list)
