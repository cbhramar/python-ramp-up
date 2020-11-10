import random

def msort(x):
    if len(x) < 2:
        return x

    result = []

    mid = len(x)//2
    y = msort(x[:mid])
    z = msort(x[mid:])

    i,j = merge(y,z,result)
  
    result += y[i:]
    result += z[j:]
    
    return result

def qsort(x):
    if len(x) < 2:
        return x

    result = []

    mid = random.randrange(0,len(x))
    y = qsort(x[:mid])
    z = qsort(x[mid:])

    i,j = merge(y,z,result)

    result += y[i:]
    result += z[j:]
    
    return result

def merge(y,z,result):
    i,j = 0,0

    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1

    return i,j

if __name__ == '__main__':
    myList = [54,26,93,17,77,31,44,55,20,1,3,2,45,54,17,77,32,3,45,2564573,132,-12]
    m = msort(myList)
    q = qsort(myList)
    print(m)
    print(q)
