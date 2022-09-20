# Find Duplicate File in System

"""
    For the duplicate files we have to group up the same content of files and for this will use dictionary 
    that will keep record of content (ie.(abcd)) and the directory path with the file name having such content
    which can be extract by the given paths with the help of split in-built function in python
    after that return the directory path of the content having more than 1 directory path.
"""

# Time Complexity = O(n) || Space Complexity = O(n)

paths = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)",
]

from collections import defaultdict


def findDuplicate(paths):
    dct = defaultdict(list)
    for path in paths:
        file = path.split(" ")
        dirpath = file[0]
        for nm in file[1:]:
            fileName, content = nm.split("(")
            dct[content].append(dirpath + "/" + fileName)
            # dct[content].append(f'{dirPath}/{fileName}')

    ans = []
    for v in dct.values():
        if len(v) > 1:
            ans.append(v)
    return ans


print(findDuplicate(paths))
