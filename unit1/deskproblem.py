import math
a=int(input("student in class1:"))
b=int(input("student in class2:"))
c=int(input("student in class3:"))
desk1=math.ceil(a/2)
desk2=math.ceil(b/2)
desk3=math.ceil(c/2)
sum=desk1+desk2+desk3
print(f"the sum is,{sum}")