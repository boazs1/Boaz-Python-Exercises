import csv
import rook


rook.start(token='7aec038f4253ae4d0056ea75d634db2f5d45a3c885cfeb527b20e0b1bcd4a86f',
           labels=None,
           git_commit='bfdd9510bfcbb7c9b990d10a9fb6d3356abad565',
           git_origin='https://github.com/boazs1/Boaz-Python-Exercises')
def rec_hist(a):
    if len(a) == 0:
        # empty string will return 26 zeros
        return [0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0]

    # wait for the recursion to retrieve the answer for shorter string (without the first letter)
    hist = rec_hist(a[1:])
    # check the ord value of the first letter
    ord_value = ord(a[0])

    # if it is a letter written in lower case:
    if 96 < ord_value < 123:
        # change from lower case to upper case [a-z] -> [A-Z]
        ord_value -= 32
    # if it is a letter in upper case:
    if 64 < ord_value < 91:
        # increment the proper counter
        hist[ord_value - 65] += 1
    # return the updated hist
    return hist


value = rec_hist(input())
print(value)