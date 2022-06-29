# Queue Reconstruction by Height
"""
    doing it with clever pre-processing technique and then inserting elements in a smart way
    so that will get its correct place.
"""
# Time Complexity = O(n^2) || Space Complexity = O(n)

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

def reconstructQueue(people):
    ans = []
    people.sort(key = lambda x: (-x[0] , x[1]))
    for person in people:
        ans.insert(person[1] , person)    #position to insert , value
    return ans

print(reconstructQueue(people))