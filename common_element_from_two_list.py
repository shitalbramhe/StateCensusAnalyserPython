l1=[1,2,3,4,5,6]
l2=[4,7,6,9]
for x in l1:
    for y in l2:
        if x==y:
            print("common element:",x)

l1=[1,2,3,4,5,6]
l2=[4,5,8,9]
x=[x for x in l1 for y in l2 if x==y]
print("common element using list comprehension:",x)