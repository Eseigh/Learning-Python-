print('only print code if all iterations completed')
num = int(input('Enter a number to check for:'))
rn = num
prime = 0
factors = []
if rn % 2 != 0:
    rn = (rn + 1)

rn = int(rn/2)
for i in range(1, rn):

    if num % i == 0:
        print("Found an Factor", i)
        factors.append(i)
        prime = i
    continue

# if (prime == 1):
#     print(f"{num} is prime")
print(factors)
if(len(factors) == 1):
    print(f"{num} is prime")