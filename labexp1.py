s=int(input("enter a no:"))
if s%2==0:
     print("the given number is even")
     t=s
     r=0
     while(s>0):
         digit=s%10
         r=r*10+digit
         s=s//10
     if(t==r):
         print("the number is pallindrome")
     else:
         print("not a pallindrome")
else:
     print("the number is odd")
     fact=1
     if s<0:
         print("negative number is not accepted")
     else:
         for i in range(1,s+1):
             fact=fact*i
         print("factorial of given number is:",fact)
     print("number of digits",len(str(fact)))    
        
