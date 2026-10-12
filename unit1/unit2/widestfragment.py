numbers =list(map(int,input("enter numbers:").split()))
current=1
maximum=1
for i in range(1,len(numbers)):
    if numbers[i]==numbers[i - 1]:
        current+=1
    else:
        current=1
maximum=max(maximum,current)
print("the length of longest string is:",maximum)