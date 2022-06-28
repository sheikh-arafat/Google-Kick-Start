cases = int(input())

for c in range(cases) :
    bag, child = map(int, input().split())
    a = list(map(int,input().split()))[:bag]
    totalCan = sum([num for num in a])
    out = totalCan % child
    print("Case #"+ str(c+1) +": "+str(out))
