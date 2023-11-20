
average = 0
sum = 0
x = 0
count = 0

while x < 100:
    count += 1
    print(count,"Count")
    sum = sum + x
    print(sum,"First Sum")
    x+=2
    print(x,"new value of x")
    average = sum / count
    print(average, "Average")
    print(sum, "Sum")


sum = 0
avg = 0
count = 0
for k in range(0, 101):
    if k % 2 == 0:
        print(k)
        sum+=k
    print(sum, "Sum")
    count = count + 1
average = sum / count
print(average, "Average")
print(sum, "Sum")


average = 0
sum = 0
x = 100
count = 0

while x>=100:
    if x%2==1:
        print(x)
        sum+=x
        count+=1
    x-=1
average=sum/count




