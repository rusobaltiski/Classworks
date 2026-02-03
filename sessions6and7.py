from dataclasses import replace
from string import punctuation

s1 = "hello world"
s2="hello world"
print(s1)
print(s2)
s1="wncwjsdjcm" #you can put weird characters
print(s1)

#we can index a string
s="banana"
print(s[1])#indexing start from zero
print(s[0]) #first letter
print(s[10//2])

#you can also index by negatives!
print(s[-1])
print(s[-6])#same as s[0]

#len function will tell you the amount of characters
print(s,len(s))

#string operators
#+ willm perform string concatenation
s1="hello"
s2="bye"
print(s1+s2)
print(s2+s1)
print(s1+", "+s2+"!!")

#you can multiply a string by an integer
print(3*s2)#nsunc song
print(s1+" "+s2+"!"*10)

#we can iterate over a string using for
#1. do the same with a while(superman)
#2. i want the result to be hhhheeeelllloooo(batman)
for c in s1:
    print(c)

i=0
while i<len(s1):
    print(s1[i])
    i +=1

s_new=""
for c in s1:
    s_new=s_new+c*4
    print(s_new)

s1="banana"
s2="bob"
#is s1>s2? or not?
print(s2>s1)#because o>a
s2="BANANA"
#is s1>s2? or not?
print(s1==s2)

#in operator it can be used to check is smaller string is in longer
s1="banana"
print("a" in s1)#true
print("ana" in s1)#true
print("bob"in s1)#false

s="0123456789"
print(s[2:4])#slice from 2 to 4(4 not included)
print(s[5:9])
print(s[:6])
print(s[4:])#456789
print(s[:])
print(s[3::2])#3579
print(s[:5:2])#024
print(s[1::2])#13579
print(s[::-1])#reverse order

#string methods
print(dir(""))
print(help("bob".capitalize))
print("hellowwwBOBOBOBOB1213!!".capitalize())
s="Hello World"
print(s.upper())
print(s.lower())
print(help(s.center))
print(s.center(30))
print(s.center(30,"*"))
#fake christmas tree
for i in range(10):
    s=("*"*(2*i+1))
    print(s.center(50))
for i in range(4):
    print("///".center(50))

#find, finds the position of substring
s="i see a cat,the cat is black,cats are nice"
print(s.find("cat"))#8 is the first occurance
print(s.find("dog"))#-1 when it cant find!
pos=0
while True:
    pos=s.find("cat",pos)
    if pos==-1:#we can find it
        break
    print(f"cat on position {pos}")
    pos+=1
print(s.count("cat"))
print(s.replace("cat","dog"))
print(s.split())

#palindromes
s="A man, a plan, a canal, Panama"
s="yo! banana boy!"
s="a nut for a jar of tuna"

#step 1 remove the punctuations
#step 2 remove the spaces
#step 3 convert to upper/lower case
#step 4 compare with the reverse
#step 5 profit

punctuation="!,.?-"
for p in punctuation:
    s=s.replace(p,"")
    print(s)
    #now spaces
    s=s.replace("","")
    print(s)
    s=s.lower()
    print(s)
    if s==s[::-1]:
        print("is palindrome")
    else:
        print("is not palindrome")
