# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    print('Hello I am the utils module')

    def printer(some_object):
        print('printer')
        print(some_object)
        print('done')

    class Shape:
        def __init__(self, id):
            self._id = id

        def __str__(self):
            return 'Shape - ' + self._id

        @property
        def id(self):
            """ The docstring for the id property """
            print('In id method')
            return self._id

        @id.setter
        def id(self, value):
            print('In set_age method')
            self._id = id

    default_shape = Shape('square')

    def _special_function():
        print('Special function')

from abc import ABC, ABCMeta, abstractmethod
class Shape(metaclass=ABCMeta):
# class Shape(ABC):
    def __init__(self, id):
        self._id = id
    @abstractmethod
    def display(self): pass
    @property
    @abstractmethod
    def id(self): pass
class Circle(Shape):
    def __init__(self, id):
        super().__init__(id)
    def display(self):
        print('Circle: ', self._id)
    @property
    def id(self):
        """ the id property """
        return self._id
c = Circle("circle1")
print(c.id)
c.display()

class ContextManagedClass(object):
    def __init__(self):
        print('__init__')
    def __enter__(self):
        print('__enter__')
        return self
    # Args exception type, exception value and traceback
    def __exit__(self, *args):
        print('__exit__:', args)
        return True
    def __str__(self):
        return 'ContextManagedClass object'
print('Starting')
with ContextManagedClass() as cmc:
    print('In with block', cmc)
    print('Exiting')
print('Done')


class ContextManagedClass(object):
    def __init__(self):
        print('__init__')
    def __enter__(self):
        print('__enter__')
        return self
    # Args exception type, exception value and traceback
    def __exit__(self, *args):
        print('__exit__:', args)
        return True
    def __str__(self):
        return 'ContextManagedClass object'
print('Starting')
with ContextManagedClass() as cmc:
    print('In with block', cmc)
    print('Exiting')
print('Done')

list1 = [1, 2, 3, 4, 5]
number_iterator = iter(list1)

print(type(number_iterator))

print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
# Once the iterator is exhausted,
# next() function raise StopIteration.
print(next(number_iterator))


