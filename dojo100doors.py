doors=[0]*100
index=[]
x=1
for j in range(100):
    for i in range(0,len(doors),x):
        if doors[i]==0:
            doors[i]+=1
        elif doors[i]==1:
            doors[i]-=1
    x+=1
for k in range(len(doors)):
    if doors[k]==1:
        index.append(k+1)
print("The following doors are open: {}".format(index))

    
    

