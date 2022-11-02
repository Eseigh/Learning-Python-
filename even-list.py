start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

even_list = range(start, end + 1)[start % 2::2]
even_arr = []
print(even_list)
for i in even_list:
    even_arr.append(i)
print(even_arr)
