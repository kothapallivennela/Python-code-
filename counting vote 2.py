n = int(input("Enter the number of voters: "))
vote = list(map(int, input("Enter the votes: ").split()))
age = list(map(int, input("Enter the ages : ").split()))
c=[0]*max(vote)
for i in range(n):
    if age[i]>=18:
        c[vote[i]-1]+=1
temp=sorted(c,reverse=True)
if temp[0]==temp[1]:
    print(-1)
else:
    print(c.index(temp[0])+1)