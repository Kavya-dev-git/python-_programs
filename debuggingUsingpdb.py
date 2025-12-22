import pdb
def calculate(a,b):
    pdb.set_trace()
    result=a+b
    result=result*2
    result=result/b
    return result
x=calculate(10,0)
print("output:",x)
