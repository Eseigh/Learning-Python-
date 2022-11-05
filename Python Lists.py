list1 = ['John', 'Paul', 'George', 'Ringo']
print(list1)

l1 = [1, 43.5, True]
l2 = ['apple', 'orange', 31]
root_list = ['Ese', l1, l2, 'Denise']
print(root_list)

t1 = (1, 'Ese', 34.5)
l1 = ['Smith', 'Jones']
l2 = [t1, l1]
t2 = (l2, 'apple')
print(t2)

vowelTuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowelTuple))

list1 = ['Ese', 'Drake', 'Durk', 'Tola']
print('list1[1]:', list1[1])
print('list1[-1]:', list1[-1])
print('list1[1:3]:', list1[1:3])
print('list[:3]:', list1[:3])
print('list[1:]:', list1[1:])

list1 = ['Ese', 'Drake', 'Durk', 'Tola']
print(list1)
list1.append('Pete')
print(list1)

list2 = ['Ese', 'Simi']
list1.extend(list2)
print(list1)

list1.insert(2, 'Drake')
print(list1)

list1 = ['Ese', 'Paul', 'George', 'Ringo']
list2 = ['Albert', 'Bob']
list3 = list1 + list2
print(list3)

list1 = ['Ese', 'Paul', 'George', 'Ringo']
print(list1)

list1.remove('George')
print(list1)

list1.pop(1)
print(list1)
