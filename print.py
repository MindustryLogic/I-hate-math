#!/usr/bin/env python
print("hello world")
print("wait 5 whole second lol")
import time
time.sleep(5)
print("The actual programm thing start here and i will not remove this part")
#wait how do i actually tell the code to seperate a equation
#ya basic math operator should seperate em
#before that do the basic of basic
def b_add():
 a = float(input("number here please"))
 b = float(input("number here please"))
 print("this is addition ")
 result = a + b
 print(f"{a}+{b}={result}")
 inf()
 
def inf():
 print("continue? Y/n")
 more = input("Y/n")
 if "Y" in more:
    b_add()
 if "n" in more:
    exit
 
b_add()