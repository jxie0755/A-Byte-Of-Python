# CS61A Exam Prep 04: List Mutation, Dictionaries, & More Trees



# List
# Q1 Lots of lists

a = [1, 2, 3, 4, 5]
a.pop(3)
b = a[:]
print('a', a)
# >>> [1, 2, 3, 5]
print('b', b)
# >>> [1, 2, 3, 5]

a[1] = b
print('a', a)
# >>> [1, [1, 2, 3, 5], 3, 5]
print('b', b) # b is a copy of a as a new object, won't be affected
# >>> [1, 2, 3, 5]

b[0] = a[:]
print('b', b)
# >>> [[1, [1, 2, 3, 5], 3, 5], 2, 3, 5]

b.pop()
b.remove(2)
print('b', b)
# [[1, [1, 2, 3, 5], 3, 5], 3]

c = [].append(b[1])
print('c', c)
# >>> None


a.insert(b.pop(1), a[-3:4:3])
print('a', a)
# >>> [1, [[1, [1, 2, 3, 5], 3, 5], 3], 3, 5]


# Trees
# Q1 Tree Recursion with trees

def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain
    the same labels the same number of times.
    >> x = tree(1, [tree(2), tree(2), tree(3)])
    >> y = tree(3, [tree(2), tree(1), tree(2)])
    >> about_equal(x, y)
    True
    >> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >> about_equal(x, z)
    False
    """
    def label_counts(t):
        if is_leaf(t):
            return {label(t): 1}
        else:
            counts = {}
            for b in branches(t) + [tree(label(t))]:
                for label, count in label_counts(b).items():
                    if label not in counts:
                        counts[label] = 0
                    counts[label] += count
            return counts
    return label_counts(t1) == label_counts(t2)


# Dictionaries
# What color is it?
# Implement decrypt, which takes in a string s and a dictionary d that contains words as values and their secret codes as keys.
# It returns a list of all possible ways in which s can be decoded by splitting it into secret codes and separating the corresponding words by spaces.

def decrypt(s, d):
    """List all possible decoded strings of s.
    >>> codes = {
    ... 'alan': 'spooky',
    ... 'al': 'drink',
    ... 'antu': 'your',
    ... 'turing': 'ghosts',
    ... 'tur': 'scary',
    ... 'ing': 'skeletons',
    ... 'ring': 'ovaltine'
    ... }
    >>> decrypt('alanturing', codes)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary
    skeletons']
    """
    if s == '':
        return []
    ms = []
    if s in d:
        ms.append(d[s])
    for k in range(1, len(s)):
        first, suffix = s[:k], s[k:]
        if first in d:
            for rest in decrypt(suffix, d):
                ms.append(d[first] + ' ' + rest)
    return ms
