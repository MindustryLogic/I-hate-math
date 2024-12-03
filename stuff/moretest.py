#/usr/bin/env python
import time
x = ['6', '+', '9', '+', '77', '-', '4']
y = '6+9+77-4'
print(type(y))
def op_id(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

start = 0
end = 0
scan = 0
alist = []    
op_lo_list = list(op_id(y, "+")) + list(op_id(y, "-")) + list(op_id(y, "*")) + list(op_id(y, "/"))
op_lo_list.sort()
print(op_lo_list)
y + '+0'
for i in y:
    print(scan)
    print(y[scan])
    if scan < len(y):
     scan = scan +1 
     print('smol')
     try:
      if y[scan].isnumeric() == False:
        print("no")
        end = scan
        alist.append(y[start:end])
        start = end
        print(alist)
     except IndexError:
         print('no u die')
         print("done")
         end = -0
         alist.append(y[start:])
         break
     else:
         print('thing is fine')
print("huhuhuhuhu")
print(alist)

long = []
long = alist[0] + alist[1]
print(long)
loong = compile(y, "<string>", "eval")
looong = eval(loong)
print(looong)
#so all this for nothing very cool