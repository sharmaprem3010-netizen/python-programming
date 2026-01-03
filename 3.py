import math

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
p = []

for num in range(start, end + 1):
    temp = num
    s = 0
    while temp > 0:
        digits = temp % 10
        s += math.factorial(digits)   # factorial of each digit
        temp //= 10
    if s == num:
        p.append(num)

print("********************************************************************")
print(f"Peterson numbers between {start} and {end}:")
print("********************************************************************")
print(p)



    
