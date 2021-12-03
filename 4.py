s=100 # GLOBAL VARIABLE
def f1():
    a=10 # local variable
    a+=1
    print(a,s)

f1()

print(s)

s=200
print(s)
def f2():
    global s
    print('global s is ',s)
    s+=1
    print('after change global is ',s)

f2()
print(s)

x=100

def t1():
    x=19
    print(x)

t1()

def t2():
    global x
    x=199
    print('now global is ',x)

t2()
print(x)