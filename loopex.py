#
# count = 0
# print('Starting')
# while count < 10:
#     print(count, '', end='')
#     count += 1
# print('Done')

# print('Print out values in a range')
# for i in range(0, 5, 2):
#     print(i)
# print('Done')

# strings with for loop
# print('Print out the letters in a string')
# for i in 'Hello world':
#     print(i)
# print('Done')
#
# # Break and Continue loop Statements
print('only print code if all iterations completed')
num = int(input('Enter a number to check for:'))
for i in range(0, num):
    if i == num:
        break
    # print(i)
    # print('Done')

    if i % 2 == 0:
        print("Found an even number",i)
    continue
# print("Found an odd number",i )

# num = int(input('Enter a number to check for:'))
# for i in range(0, 6):
#     if i == num:
#         break
#     print(i, '', end='')
# else:
#     print('All iterations successful')
