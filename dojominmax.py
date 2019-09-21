numbers=[-5, 23, 0, -9, 12, 99, 105, -43]
min=0
max=0
avg=0
sum=0
x=0
for num in numbers:
    if x==0:
        min=num
        max=num
        x+=1
    else:
        if num<min:
            min+=num-min
            x+=1
        elif num>max:
            max+=num-max
            x+=1
        else:
            x+=1
            continue
for num in numbers:
    sum+=num
avg=sum/(len(numbers))

print (min,max,avg)
