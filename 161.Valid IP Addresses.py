# valid IP Addresses

string = "1921680"


def validIPAddresses(string):
    ipAddresses = []

    for i in range(1, min(len(string), 4)):
        currentIp = ["", "", "", ""]
        currentIp[0] = string[:i]
        if not isValid(currentIp[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIp[1] = string[i:j]
            if not isValid(currentIp[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIp[2] = string[j:k]
                currentIp[3] = string[k:]
                if isValid(currentIp[2]) and isValid(currentIp[3]):
                    ipAddresses.append(".".join(currentIp))
    return ipAddresses


def isValid(string):
    stringAsInt = int(string)
    if int(string) > 255:
        return False
    return len(string) == len(str(stringAsInt))


print(validIPAddresses(string))
