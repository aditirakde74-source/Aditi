n=int(input("enter total pins:"))
k=int(input("enter total balls:"))
pins=["i"]*n
for i in range (k):
    start,end=map(int,input(f"enter range for ball{i+1}:".split()))
    for j in range(start-1,end):
        pins[j]="."
print("".joins(pins))
     