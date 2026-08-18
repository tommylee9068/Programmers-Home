def solution(arr):
    a = []
    i = 0
    while i < len(arr):
        if len(a) == 0:
            a.append(arr[i])
            i += 1
        elif len(a) != 0 and a[-1] < arr[i]:
            a.append(arr[i])
            i += 1
        elif len(a) != 0 and a[-1] >= arr[i]:
            a.pop(-1)
    return a
            
    
    
    
    # stk = []
    # return stk