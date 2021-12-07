#write a python program which will keep adding a stream of numbers entered by the user. The adding stops 
#as soon as the user press quit/q key on the keyboard (store calculator)


sum=0
while (True):
    num=input("enter the price: \n")
    if (num!='q'):
        sum=sum+int(num)

    else:
        print("Quit")
        print(f"Total is{sum}")
        break







