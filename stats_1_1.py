import random
#This code eliminates input that is not number and is strings
while True:
    try:
        num=int(input("Please enter a number:"))
        break
    except:
        print("Oops!  That was no valid number")
    continue    
count=0
tot=0
smallest=None
largest=None
while True: 
             
    x=random.random()
    count=count+1
    tot=tot+x
    avg=tot/count
    print(x)  
    if count==num:
        break
    
    if smallest is None:
        smallest=x
    elif x<smallest:
        smallest=x
    if largest is None:
        largest=x
    elif x>largest:
        largest=x
             
print("Average is:", avg, "Smallest is:", smallest, "Largest is:", largest) 
