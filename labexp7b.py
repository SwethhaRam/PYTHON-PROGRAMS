class NegValue(Exception):
    pass
try:
    name=input("ENTER YOUR NAME : ")
    age=int(input("ENTER YOUR AGE : "))
    if age<0:
        raise NegValue
    marks=[]
    for i in range(0,6):
        mark=float(input("ENTER THE MARKS : "))
        marks.append(mark)
    dict_={"NAME":name,"AGE":age,"MARKS":marks}
    print("DETAILS : \n",dict_)
except NegativeValue:
    print("AGE IS IN NEGATIVE INTEGER")

 
