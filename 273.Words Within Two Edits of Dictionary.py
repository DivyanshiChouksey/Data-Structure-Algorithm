# Words Within Two Edits of Dictionary

queries = ["word", "note", "ants", "wood"]
dictionary = ["wood", "joke", "moat"]

"""
    Check each string of queries with each string of dictionary and also we keep record of edits  
    Go through the queries and dictionary and by using zip function check each character of both words and 
    if character is not equal then count it as edits after that check if edits is less than or equals to two 
    then append that string in our ans and at the end return the ans. 
"""
# Time Complexity = O(q.d.n) , q = len(queries) ,d=len(dictionary)
# Space Complexity = O(q)    , n = len(average string of queries)


def twoEditWords(queries, dictionary):
    ans = []
    for word in queries:
        for dct in dictionary:
            edit = 0
            for w, d in zip(word, dct):
                if w != d:
                    edit += 1
                    if edit > 2:
                        break
            if edit <= 2:
                ans.append(word)
                break

    return ans


print(twoEditWords(queries, dictionary))
