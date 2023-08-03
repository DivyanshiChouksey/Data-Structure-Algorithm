# Letter Combinations of a Phone Number


digits = "23"

def letterCombinations(digits):
    if len(digits)==0:
        return []

    dct = {
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]
        }

    ans = []
    def helper(tmp,curDigit): 
        if len(tmp) == len(digits):
            ans.append(tmp)
            return

        for ch in dct[curDigit[0]]:
            helper(tmp+ch,curDigit[1:])

    helper("",digits)
    return ans


print(letterCombinations(digits))
