def is_ascending(numbers):
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
          return true
numbers=list(map(int,input("enter the list of numbers(comma-seperated):").split(',')))
if is_ascending(numbers):
    print("the list is in ascending order")
else:
    print("the list is not in ascending order")
                           
