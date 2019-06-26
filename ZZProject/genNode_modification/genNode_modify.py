# This is a practice to revise all genNode function for Leetcode LinkedList question
# The orignal genNode function supports *nodes as a number of parameter or nodes as a List
# It is later decided that to remove *nodes option and force to use single List[int] parameter.

# Therefore there is a need to add '[' and ']' to all previous finished questions with genNode implemented with *nodes.
# This is a good chance to practice regular expression and file reading / modification.

import re
import os

# to match find the genNode in application
raw = r'([g][e][n][N][o][d][e][(])([[][0-9\,\s]*[]])([)])'
to_match = re.compile(raw)

# Quick test on groups
# test = 'genNode([1,2,3, 4, 5])'  # may mix with spapce
# test_output = re.match(to_match, test)
# print(test_output.groups())
# >>> ('genNode(', '[1,2,3, 4, 5]', ')')


# Source dir for leetcode folder
sourcedir = 'D:/Documents/GitHub/Learning_Python/LeetCode'

for sub_dir in os.listdir(sourcedir):
    full_sub_dir = sourcedir + '/' + sub_dir
    if not os.path.isdir(full_sub_dir):
        with open(full_sub_dir) as f:
            content = f.read()
        print(content)


