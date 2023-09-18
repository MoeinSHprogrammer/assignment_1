import math


a = int(input())
b = int(input())

op = input()

res = None
if op == "+":
    res = a + b

if op == "-":
    res = a - b

if op == "/":
    if b != 0:
        res = a / b
    else:
        ('divided by zero')

if op == "*":
    res = a * b

if op == "pow":
    res = a ** b

if op == "sin":
    res = math.sin(a)

if op == "cos":
    res = math.cos(a)

if op == "tan":
    res = math.tan(a)

if op == "cot":
    res = math.cos(a) / math.sin(a)

if op == "radical":
    res = math.sqrt(a)
    
if res != None:
    print(res)
else:
    print('Wrong Operation!')