#!/usr/bin/env python
#GPL-3.0-only or GPL-3.0-or-later
print("hello world")
def mode_sele():
    print("ari for arithmetic(basic math), exit to exit")
    mode = input("type mode here: ")
    match mode:
        case "ari":
            ari()
        case "exit":
            exit
def ari():
    print("Arithmetic mode a.k.a +-*/ selected")
    global eq
    eq = input("equation here: ")
    step_comfirm()
    if step_ava == False:
        result = eval(compile(eq, "<string>", "eval"))
        print(f"{eq}={result}")
    else:
        print("makin'")
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
mode_sele()