smallest = None
print("before =",smallest)
for i in [41,27,18,1,2,5,78,55,627,78,99,77,66,55,121234,545]:
    if smallest is None or i<smallest:
        smallest= i
    print("loop=",i,smallest)
print("smallest",smallest)
