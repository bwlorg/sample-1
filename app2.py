
#function with out args and with out return type

def fun1():
    print("function with out args and with out return type...fun1")


#function with  args and with out return type

def fun2(a,b):
    print("function with args and with out return type...fun2",a," ," ,b)

#function with out args and with  return type

def fun3():
    print("function with out args and with  return type...fun3")
    return 12

#function with  args and with  return type
def fun4(x,y):
    print("function with  args and with  return type...fun4",x," ," ,y)
    z=x+y
    return z

fun1()
fun2(100,200)
print(fun3())
print(fun4(12,15))
