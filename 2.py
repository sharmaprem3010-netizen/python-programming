# Automorphic numbers in a range without using endswith()

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

automorphic_list = []

for num in range(start, end + 1):
    square = num * num
    digits = len(str(num))  # count digits in num
    if square % (10 ** digits) == num:  # compare last digits
        automorphic_list.append(num)

print("********************************************************************")
print(f"Automorphic numbers between {start} and {end}:")
print("********************************************************************")
print(automorphic_list)
