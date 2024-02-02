a=[1,2,3,4]
a.append([1,2])
a.extend([1,2])
print(a)

a=[1,2,3,4]
a.remove(a[3])
print(a)

a[0]='ram'
print(a)
del a[0]
print(a)