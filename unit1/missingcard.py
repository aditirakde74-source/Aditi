n =int(input("enter n:"))
cards=list(map(int,input("enter remaining card numbers:").split()))
expected_sum = n*(n+1)/2
actual_sum=sum(cards)
missing_card = expected_sum - actual_sum
print(f"the missing card={missing_card}")
