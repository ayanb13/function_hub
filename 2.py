def f1():
    '''
    this function is created by amitava
    its written on 3rd dec 2021 
    new corona coming
    megha having biebari vojon....
    '''
    print('i am a function  ')


f1()

print('the doc is ',f1.__doc__) # MAGIC VARIABLE
f1()
def calc(a,b):
    c=a+b
    print('the sum is '+str(c))

calc(11,22)

def calc_better(a,b):
    return a+b

x=calc_better(3,4)
print('the sum is ',x)

def two_work(a,b):
    return a+b

print('the sum is ',two_work(11,22))
print('the name is ',two_work('amitava','chatterjee'))


def special_calc(x,y):
    q=x+y
    w=x-y
    d=x*y
    v=x/y
    return q,w,d,v# by default it will return a single tuple


t1,t2,t3,t4=special_calc(22,4)
print(t1,t2,t3,t4)

k=special_calc(12,10)
print(type(k))

for i in k:
    print(i)

f=calc(11,22)
print(type(f))


def create_list(a,b,c,d,e):
    l=[a,b,c,d,e]
    return l

o=create_list(11,22,33,44,55)
print(type(o))

def create_tuple(l):
    t=(l[0],l[1],l[2],l[3],l[4])
    return t

w=create_tuple(o)
print(type(w))
for i in w:
    print(i)

def init_fun(a=100,b=11.33):
    print(a,b)

init_fun(1)







