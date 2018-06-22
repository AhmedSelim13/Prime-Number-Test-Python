your_number = input("Please insert your number for test: ")
is_not = 0
c = int(your_number ** (1/2))
if x % 2 == 0:
— is_not = 1
— break
for y in range(3,c,2):
— if x % y == 0:
— — is_not = 1
— — break
if is_not == 1 and x > 2:
— print(str(your_number) + " is not prime.")
else:
— print(str(your_number) + "is prime.")
