largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest :
            smallest = value
    return smallest
def max(values):
    largest = None
    for value in values:
        if largest is None or value > largest:
            largest = value
    return largest
print("Maximum", largest)
print("Minimun", smallest)
