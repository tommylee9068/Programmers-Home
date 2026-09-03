def solution(myStr):
    myStr = myStr.replace('a', ' ')
    myStr = myStr.replace('b', ' ')
    myStr = myStr.replace('c', ' ')
    result = myStr.split()
    if len(result) == 0:
        return ["EMPTY"]
    else:
        return myStr.split()
    
    