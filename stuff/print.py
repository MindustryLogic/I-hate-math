#!/usr/bin/env python
#GPL-3.0-only or GPL-3.0-or-later
print("hello world")
print("wait 5 whole second lol")
import time
time.sleep(5)
print("The actual programm thing start here and i will not remove this part")
#wait how do i actually tell the code to seperate a equation
#ya basic math operator should seperate em
#before that do the basic of basic
def b_add():
 input1 = float(input("number here please "))
 input2 = float(input("number here please "))
 print("this is addition ")
 result = input1 + input2
 print(f"{input1}+{input2}={result}")
 inf()
 
def op_id(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i
 
def inf():
 print("continue? Y/n")
 more = input("Y/n: ")
 if "Y" in more:
    b_add()
 if "n" in more:
    mode_sele()
 
 
def mode_sele():
 print("work for currently working stuff, exp for indev mode ig, and exit kill the programm")
 mode = input("uh what mode u want use type it exactly idk ")
 if "work" in mode:
   b_add()
 if "exit" in mode:
    exit
 else :
    temp()
    
    
def temp():
    eq_input = input("type equation here: ")
    eq_input_first_fix = ""
    op_included_start = eq_input.find("+" or "-", 0, 1)
    eq_input_1st_num = eq_input[0]
    if "-1" == op_included_start:
       eq_input_first_fix = "9"
    else :
       eq_input_first_fix = eq_input

    print(op_included_start)
    print(eq_input_1st_num)
    print(eq_input[0])
    print(eq_input_first_fix)
    print(list(op_id(eq_input, "+")))
    print(list(op_id(eq_input, "-")))
    print(list(op_id(eq_input, "*")))
    print(list(op_id(eq_input, "/")))
    num_count = len(list(op_id(eq_input, "+"))) + len(list(op_id(eq_input, "-"))) + len(list(op_id(eq_input, "*"))) + len(list(op_id(eq_input, "/")))
    print(num_count)
    mode_sele()

    

mode_sele()