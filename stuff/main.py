#!/usr/bin/env python
#GPL-3.0-only or GPL-3.0-or-later
print("hello world")
import math
def mode_sele():
    #this part just let you select mode
    print("ari for arithmetic(basic math), exit to exit, if you type thing not in here it will also quit")
    mode = input("type mode here: ")
    match mode:
        case "ari":
            ari()
        case "exit":
            exit
def ari():
    #self explained
    latter_detect = 0
    print("Arithmetic mode a.k.a +-*/ selected")
    global eq
    eq = input("equation here: ")
    for i in eq:
        if eq[latter_detect].isalpha == False:
            latter_detect = latter_detect +1
        else:
            print("AY BRO THERE'S A LATTER IN HERE")
            return
    step_comfirm()
    if step_ava == False:
        result = eval(compile(eq, "<string>", "eval"))
        print(f"{eq}={result}")
        mode_sele()
    else:
        result = eval(compile(eq, "<string>", "eval"))
        step_show = input("show steps? (Y/n): ")
        match step_show:
            case "Y":
                print("makin")
                step_by_step()
                print(f"={result}")
                mode_sele()
            case "n":
                print(f"{eq}={result}")
                mode_sele()
def step_comfirm():
    global step_ava
    if len(list(op_id(eq, "*")) or list(op_id(eq, "/")) or list(op_id(eq, "(")) or list(op_id(eq, ")"))) != 0:
        step_ava = bool(True)
    else:
        step_ava = bool(False)
        
def op_id(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

def step_by_step():
    start = 0
    end = 0
    eq_sep = []
    eq_sep_tu = ()
    scan = 0
    for i in eq:
        if scan < len(eq):
            scan = scan+1
            try:
                if eq[scan].isnumeric() == False:
                    end = scan
                    eq_sep.append(eq[start:end])
                    eq_sep.append(eq[end:end+1])
                    start = end+1
            except IndexError:
                eq_sep.append(eq[start:])
    eq_sep_tu = tuple(eq_sep)
    print(eq_sep)
    print(eq_sep_tu)
    #The step part
    n = 1
    print("Rule of thumb:() then * or / then + or -")
    #First make program know where operators are
    #Then order the thing
    #print result
    
mode_sele()

