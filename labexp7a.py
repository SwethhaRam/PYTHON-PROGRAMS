try:
    s=int(input("ENTER RANGE :  "))
    list_=[]
    for i in range(0,s):
        num=int(input())
        list_.append(num)
    r=int(input("ENTER THE INDEX VALUE : "))
    print("THE ELEMENT AT ",r," IS ",list_[r])
except IndexError:
    print("INDEX EXCEEDS LIMIT !  ")
    print("THE LAST INDEX IS : ",len(list_) -1)
