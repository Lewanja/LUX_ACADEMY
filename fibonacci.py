previous =0
current=1
neww=0
while current <1000:
    neww= current +previous
    previous = current
    current = neww
    
    
    print(current)

x=int(input("Enter a number:"))
if x==current:
    print(f"the number {x} is in the fibonacci series")

else:
    print(f"the number {x} is not in the fibonacci series")
