#left pascal +right pascal
#left pascal:
#one increasing triangle and decreasing space 
#one decreasing triangle and increasing space

#right pascal:
#one decreasing space and one increasing triangle
#once increasing space and one decreasing triangle

#left pascal :
n=5
for i in range(n-1):
    for j in range(i+1):
        print("*",end="")
    for j in range(i,n):
        print(" ",end="")
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(n):
    for j in range(i,n):
        print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
#    print()
