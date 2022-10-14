#  issue - lower case and upper case


def harry(str, m, n):
    le = len(str)
    org = str.upper()
    str = str.upper()
    turn = 0
    for i in str:
        str3 = str[-m:]  # last n letters
        str = str.replace(" ", "")[:-m]
        str = str3 + str
        print(str)
        if org != str:
            turn = turn + 1
            str4 = str[-n:]
            str = str.replace(" ", "")[:-n]
            str = str4 + str
            print(str)
            turn = turn + 1
        if org == str:
            break
    print(turn)


str = input("Enter the string")
m = int(input("Enter the value of m"))
n = int(input("Enter the value of n"))
harry(str, m, n)
