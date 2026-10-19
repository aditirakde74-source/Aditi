string=input("enter the string:")
result=""
for i in range(len(string)):
    if i%3!=0:
     result=result+string[i]
print("result=",result)