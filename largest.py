largest = None
print("before =",largest)
for i in [41,27,18,1,2,5,78,55,627,78,99,77,66,55,121234,545]:
    if largest is None or i>largest:
        largest= i
    print("loop=",i,largest)
print("largest",largest)
