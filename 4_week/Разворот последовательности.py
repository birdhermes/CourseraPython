def posled():
    n = int(input())
    result = []
    while n != 0:

        result.append(n)
        posled()



    return result


posled()
