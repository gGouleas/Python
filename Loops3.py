a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#script 1
for i in a:
    if i<5:
        print(i,end=" ")
    
#script 2
print("\n")
n = int(input("Give a number:"))
for i in a:
    if i<n:
        print(i,end=" ")
    
