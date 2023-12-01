x = int(input("x ="))
y = int(input("y ="))
z = int(input("z="))
n = int(input("n="))
ans =[]
for i in range (0,x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if n != (i+j+k):
                ans.append([i,j,k])
print(ans)