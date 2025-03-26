#sum of natural numbers
# var to get number:
n = int(input("enter a number that you want the sum of: "))
#sum work-out:
sum = 0
for i in range(1, n+1):
    sum = sum + i
    print("\n sum =", sum) # printing the sum

# reversed string:
# input for a string
str1 = input("enter your string to be reversed: ")
str2 = (' ')
#loop for reversing string:
for i in str1:
    str2= i + str2
print(f"\n original {str1}")
print(f"\n reversed {str2}")

# reverse numbers:
n = int(input("enter a number for n: "))
#print numbers from n to 1
print("numbers form {0} to {1} are:" .format(n,1))
# start = n, end = 0, step = -1 - how many step you want ot skip
for i in range(n, 0, -1):
    print("\n", i)
    

