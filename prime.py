a=7
count=0
for i in range(2,a):
    if a%i==0:
        count+=1
if count==0:
    print("Prime Number")
else:
    print("Not a Prime Number")