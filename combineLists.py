Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten (lists):
    result = []
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            result.append(lists[i][j])
    return result

print flatten(n)
