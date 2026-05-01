#PowerOf8
def power8(n):
    if n <= 0:
        return False
    if (n & (n - 1)) != 0:
        return False
    
    pos = 0
    while n > 1:
        n >>= 1
        pos += 1
    
    return pos % 3 == 0

x = int(input("Enter your number: "))
if power8(x):
    print(f"Yes, {x} is the power of 8")
else:
    print(f"No, {x} is not the power of 8")