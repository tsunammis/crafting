# #############################
# Access a Dictionary Element
# #############################

# BAD
d = {'hello': 'world'}
if d.has_key('hello'):
    print d['hello']    # prints 'world'
else:
    print 'default_value'

# Good
d = {'hello': 'world'}
print d.get('hello', 'default_value') # prints 'world'
print d.get('thingy', 'default_value') # prints 'default_value'

# Or:
if 'hello' in d:
    print d['hello']

# #############################
# Iterating over dictionary key and value pairs (dict.iteritems)
# #############################
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for k, v in m.iteritems():
    print '{}: {}'.format(k, v)

# #############################
# Zipping and unzipping lists and iterables
# #############################
a = [1, 2, 3]
b = ['a', 'b', 'c']
z = zip(a, b) # [(1, 'a'), (2, 'b'), (3, 'c')]
zip(*z) # [(1, 2, 3), ('a', 'b', 'c')]

# #############################
# Named tuples (collections.namedtuple)
# #############################

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1.0, y=2.0)

# #############################
# Cartesian products (itertools.product)
# #############################
for p in itertools.product([1, 2, 3], [4, 5]):
    print(p)
# (1, 4)
# (1, 5)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)

for p in itertools.product([0, 1], repeat=4):
    print(''.join(str(x) for x in p))

# 0000
# 0001
# 0010
# 0011
# 0100
# 0101
# 0110
# 0111
# 1000
# 1001
# 1010
# 1011
# 1100
# 1101
# 1110
# 1111

# #############################
# Combinations and combinations with replacement (itertools.combinations and itertools.combinations_with_replacement)
# #############################

for c in itertools.combinations([1, 2, 3, 4, 5], 3):
    print(''.join(str(x) for x in c))

# 123
# 124
# 125
# 134
# 135
# 145
# 234
# 235
# 245
# 345

for c in itertools.combinations_with_replacement([1, 2, 3], 2):
    print(''.join(str(x) for x in c))

# 11
# 12
# 13
# 22
# 23
# 33

# #############################
# Permutations (itertools.permutations)
# #############################

for p in itertools.permutations([1, 2, 3, 4]):
    print(''.join(str(x) for x in p))

# 1234
# 1243
# 1324
# 1342
# 1423
# 1432
# 2134
# 2143
# 2314
# 2341
# 2413
# 2431
# 3124
# 3142
# 3214
# 3241
# 3412
# 3421
# 4123
# 4132
# 4213
# 4231
# 4312
# 4321

# #############################
# Short Ways to Manipulate Lists
# #############################

# BAD
# Filter elements greater than 4
a = [3, 4, 5]
b = []
for i in a:
    if i > 4:
        b.append(i)

# Good
a = [3, 4, 5]
b = [i for i in a if i > 4]
# Or:
b = filter(lambda x: x > 4, a)

# BAD
# Add three to all list members.
a = [3, 4, 5]
for i in range(len(a)):
    a[i] += 3

# Good
a = [3, 4, 5]
a = [i + 3 for i in a]
# Or:
a = map(lambda i: i + 3, a)

# #############################
# Naming slices (slice(start, end, step))
# #############################
a = [0, 1, 2, 3, 4, 5]
LASTTHREE = slice(-3, None)
LASTTHREE # slice(-3, None, None)
a[LASTTHREE] # [3, 4, 5]
