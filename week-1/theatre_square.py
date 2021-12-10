n,m,a = input().split()
 
left = int(m)
top = int(n)
dim = int(a)
 
total_left = 0
total_top = 0
 
if left%dim==0: 
    total_left=left//dim
else: 
    total_left=left//dim+1 
 
if top%dim==0: 
    total_top=top//dim
else: 
    total_top=top//dim+1 
 
print(total_top*total_left)
