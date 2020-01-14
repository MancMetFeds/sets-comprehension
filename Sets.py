print("type union, intersection or relativecomplement to use")

A=[1,2,3,4,5]
B=[4,5,6]
T=[]
i=0
for i in range(100):
    i+=1
    T.append(i)
print("A="+str(A))
print("B="+str(B))
print("T="+str(T))
union=[]
for items in A:
    union.append(items)
for items in B:
    if items not in union:
        union.append(items)
    else:
        pass
intersection=[]
for items in A:
    if items in B:
        intersection.append(items)
    else:
        pass
relativecomplement=[]
for items in B:
    if items in A:
        pass
    else:
        relativecomplement.append(items)
