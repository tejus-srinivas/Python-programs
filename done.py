num = 0
tot = 0.0
while True:
    a = input("enter a number = ")
    if a == 'done':
        break
    try:
        b = float(a)
    except:
        print("ivalid input")
        continue
    print(b)
    num = num + 1
    tot = tot + b

print("all done ")
print(tot,num,tot/num)
