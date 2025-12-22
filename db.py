import pdb
def multiply(a,b):
    c=a*b
    d=c+5
    return d
def calculate(a,b):
    pdb.set_trace()
    x=a+b
    y=multiply(x,b)
    z=y/b
    return z
result=calculate(10,0)
print("result:",result)
