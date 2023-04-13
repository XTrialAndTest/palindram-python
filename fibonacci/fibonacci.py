def fibonacci(first,second,end):
    list=[first,second]
    nextvalue=list[-1]+list[-2]
    while len(list)<end:
        nextvalue=list[-1]+list[-2]
        list.append(nextvalue)
    return list
fibonacci(1 , 3, 5)
    