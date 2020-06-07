CHAR_LENGTH = 8
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
charToIndex = dict()
for index, value in enumerate(chars):
    charToIndex[value] = index


def encode64(s):
    res = []
    N = len(s)
    padding = 0
    for i in range(0, N, 3):
        j = i
        countBit = 0
        val = 0
        while j < N and j < i + 3:
            val = val << CHAR_LENGTH
            val = val | ord(s[j])
            countBit += CHAR_LENGTH
            j += 1

        # if this group has less than 3 chars
        padding = countBit % 3

        while countBit > 0:
            if countBit >= 6:
                encodedChar = chars[(val >> (countBit - 6)) & 63]
                countBit -= 6
            else:
                encodedChar = chars[(val << (6 - countBit)) & 63]
                countBit = 0
            res.append(encodedChar)

    for _ in range(padding):
        res.append("=")

    return ''.join(res)


def decode64(s):
    val = 0
    N = 0
    res = []
    for c in s:
        if c in charToIndex:
            val = (val << 6) + charToIndex[c]
            N += 6
        else:
            val = val >> 2
            N -= 2
    for i in range(0, N, 8):
        asciiVal = (val >> (N - (i + 8))) & 255
        res.append(chr(asciiVal))
    return ''.join(res)


print(decode64(encode64("MENON")))
print(decode64(encode64("geeksforgeeks")))
