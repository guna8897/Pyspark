def add(a,b):
    result=a+b
    print(result)
def sub(a,b):
    result=a-b
    print(result)

def mul(a,b):
    result=a*b
    print(result)

def div(a,b):
    result=a/b
    print(result)

def mod(a,b):
    result=a%b
    print(result)

def exp(a,b):
    result=a**b
    print(result)

def fld(a,b):
    result=a//b
    print(result)

def rst(a,b):
    result=a>>b
    print(result)

def lst(a,b):
    result=a<<b
    print(result)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operator: ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="%":
    mod(a,b)
elif op=="**":
    exp(a,b)
elif op=="//":
    fld(a,b)
elif op==">>":
    rst(a,b)
elif op=="<<":
    lst(a,b)

else:
    div(a,b)