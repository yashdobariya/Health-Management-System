
    # Health Management System
 
import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if (k==1):
        l=int(input("Press 1 for Excerscie 2 for Food:"))
        if (l==1):
            value=input("tyre here\n")
            with open("yash-ex.txt","a") as y:
                y.write(str([str(gettime())]) + ": "+ value +"\n")
            print("You Written Succesfully")
        elif (l==2):
            value=input("tyre here\n")
            with open("yash-food.txt","a") as y:
                y.write(str([str(gettime())])+": "+value+"\n")
            print("You Written Succesfully")

    elif(k==2):
        l = int(input("Press 1 for Excerscie 2 for Food:"))
        if (l == 1):
                value=input("tyre here\n")
                with open("dixit-ex.txt","a") as y:
                    y.write(str([str(gettime())])+": "+value+"\n")
                print("You Written Succesfully")
        elif (l==2):
                value=input("tyre here\n")
                with open("dixt-food.txt","a") as y:
                    y.write(str([str(gettime())])+": "+value+"\n")
                print("You Written Succesfully")
    elif (k==3):
        l = int(input("Press 1 for Excerscie 2 for Food:"))
        if (l == 1):
            value = input("tyre here\n")
            with open("darshil-ex.txt", "a") as y:
                y.write(str([str(gettime())]) + ": " + value + "\n")
            print("You Written Succesfully")
        elif (l == 2):
            value = input("tyre here\n")
            with open("darshil-food.txt", "a") as y:
                y.write(str([str(gettime())]) + ": " + value + "\n")
            print("You Written Succesfully")
def retrieve(k):
    if k==1:
        l=int(input("Press 1 for Excerscie 2 for Food:"))
        if (l==1):
            with open("yash-ex.txt",) as y:
                for i in y:
                    print(i,end="")
        elif (l==2):
            with open("yash-food.txt",) as y:
                for i in y:
                    print(i,end="")
    if k==2:
        l=int(input("Press 1 for Excerscie 2 for Food:"))
        if (l==1):
            with open("dixit-ex.txt",) as y:
                for i in y:
                    print(i,end="")
        elif (l==2):
            with open("dixit-food.txt",) as y:
                for i in y:
                    print(i,end="")
    if k==3:
        l=int(input("Press 1 for Excerscie 2 for Food:"))
        if (l==1):
            with open("darshil-ex.txt",) as y:
                for i in y:
                    print(i,end="")
        elif (l==2):
            with open("darshil-food.txt",) as y:
                for i in y:
                     print(i,end="")


print("Helth Management System:")
a=int(input("Press 1 for Log the value and 2 for Retrieve:"))

if a==1:
    b=int(input("Press 1 for Yash 2 for Dixit 3 for Darshil:"))
    take(b)
else:
    b=int(input("Press 1 for Yash 2 for Dixit 3 for Darshil:"))
    retrieve(b)
