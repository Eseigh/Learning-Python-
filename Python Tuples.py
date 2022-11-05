tup1 = (1, 3, 5, 7)
print('tup1:\t', tup1)
print('tup1[0]:\t', tup1[0])
print('tup1[1]:\t', tup1[1])
print('tup1[2]:\t', tup1[2])
print('tup1[3]:\t', tup1[3])

tup1 = (1, 3, 5, 7)
print('tup1[1:3]:\t', tup1[1:3])
print('tup1[:3]:\t', tup1[:3])
print('tup1[1:]:\t', tup1[1:])
print('tup1[::-1]:\t', tup1[::-1])

tup2 = (1, 'John', True, -23.45)
print(tup2)

tup3 = ('Maguire', 'Messi ', 'Ronaldo', 'Marcelo', 'Haaland')
for x in tup3:
    print(x)

tup3 = ('Maguire', 'Messi ', 'Ronaldo', 'Marcelo', 'Haaland')
print('len(tup3):\t', len(tup3))  # returns length
print(tup3.count('apple'))  # returns 2
print(tup3.index('pear'))  # returns 1

tup3 = ('Maguire', 'Messi ', 'Ronaldo', 'Marcelo', 'Haaland')
if 'orange' in tup3:
    print('orange is in the Tuple')

tuple1 = (1, 3, 5, 7)
tuple2 = ('Davido', 'Burna', 'Wizkid', 'Asake')
tuple3 = (42, tuple1, tuple2, 5.5)
print(tuple3)
