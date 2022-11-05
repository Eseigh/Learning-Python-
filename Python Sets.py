basket = {'apple', 'orange', 'apple', 'pear',
          'orange', 'banana'}
print(basket)

set1 = {1, 2, 3}
print(set1)

basket = {'apple', 'orange', 'banana'}
print('apple' in basket)  # Check if ‘apple’ is a member set
basket.update(['apricot', 'mango'])  # Adding more item
print(basket)
print(len(basket))  # Finding length of Set
basket.discard('apricot')  # Removing apricot
print(basket)
basket.clear()  # remove all elements
print(basket)

s1 = {7, (1, 2, 3)}  # Nesting a Tuple in Set
print(s1)

# Nesting Frozenset
s2 = {7, (1, 2, 3), frozenset({4, 5, 6})}
print(s2)

s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}
print('Union:', s1 | s2)  # Union
print('Intersection:', s1 & s2)  # Intersection
print('Difference:', s1 - s2)  # Difference
# Symmetric Difference
print('Symmetric Difference:', s1 ^ s2)
