# list comprehension
lst = [i * i for i in range(10)]
print(lst)
lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)

'''
List Comprehension

List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
Syntax:

List = [Expression(item) for item in iterable if Condition]

Expression: It is the item which is being iterated.

Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

Condition: Condition checks if the item should be added to the new list or not.
'''
print()
print()

# tuple
tup = (1, 2, 3, 4, "yes", "no")
print(type(tup), tup)

# single element in the tuple registered as int/str.
# putting comma solves the problem.
tup1 = (1)
tup2 = (1,)
print(type(tup1), tup1)

# concatenate tuple
tup3 = (4243, 4256)
tup4 = (123, 234)

addtup = tup3 + tup4 # new tuple is created

print(tup3)
print(tup4)
print(addtup)





