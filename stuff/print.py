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
 match mode:
  case "work":
   b_add()
  case "exit":
    exit
  case "exp":
    temp()
    
    
def temp():
    eq_input = str(input("type equation here: "))
    global eq_input_first_fix
    eq_input_first_fix = ""
    op_included_start = eq_input.find("+" or "-", 0, 1)
    eq_input_1st_num = eq_input[0]
    if -1 is op_included_start:
       eq_input_first_fix = "+" + eq_input
       print("it have a thing)")
    else :
       eq_input_first_fix = eq_input
       print("it no thing")

    print(op_included_start)
    print(type(op_included_start))
    print(eq_input_1st_num)
    print(eq_input[0])
    print(eq_input_first_fix)
    print(list(op_id(eq_input, "+")))
    print(list(op_id(eq_input, "-")))
    print(list(op_id(eq_input, "*")))
    print(list(op_id(eq_input, "/")))
    print(list(op_id(eq_input_first_fix, "+")))
    print(list(op_id(eq_input_first_fix, "-")))
    print(list(op_id(eq_input_first_fix, "*")))
    print(list(op_id(eq_input_first_fix, "/")))
    num_count = len(list(op_id(eq_input, "+"))) + len(list(op_id(eq_input, "-"))) + len(list(op_id(eq_input, "*"))) + len(list(op_id(eq_input, "/")))
    fix_num_count = len(list(op_id(eq_input_first_fix, "+"))) + len(list(op_id(eq_input_first_fix, "-"))) + len(list(op_id(eq_input_first_fix, "*"))) + len(list(op_id(eq_input_first_fix, "/")))
    print(num_count)
    print(fix_num_count)
    basic_cal()
    mode_sele()

def basic_cal():
   scan = 0
   eq_list = []
   for i in eq_input_first_fix:
      eq_list.append(eq_input_first_fix[scan:scan + 1])
      scan = scan+1
   print(eq_list)
   op_lo_list = list(op_id(eq_input_first_fix, "+")) + list(op_id(eq_input_first_fix, "-")) + list(op_id(eq_input_first_fix, "*")) + list(op_id(eq_input_first_fix, "/"))
   op_lo_list.sort()
   print(op_lo_list)
mode_sele()