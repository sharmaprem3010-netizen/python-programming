num=int(input("Enter the number you wish:"))
print("********************************************************************")
print(f"the number you put is this {num}")
print("********************************************************************")
print("Now i am going to show you the result of my hard work")
print("********************************************************************")
length=len(str(num))
print(f"this numbers length is {len(str(num))}")
print("********************************************************************")
power = int(input("Enter the power of the number"))
print("********************************************************************")
print(f"the power of the numbe is {num**power}")
print("********************************************************************")
sum=0
tem=num
while(tem!=0):
    rem=tem%10
    sum=sum+(rem**length)
    tem=tem//10
print(f"The number {num} length,power,digit,sum={sum}")

          
