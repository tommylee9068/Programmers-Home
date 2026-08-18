def solution(l, r):
    a = []
    for i in range(l, r+1):
        if i % 5 == 0 and '1' not in str(i) and '2' not in str(i) and '3' not in str(i) and '4' not in str(i) and '6' not in str(i) and '7' not in str(i) and '8' not in str(i) and '9' not in str(i):
            a.append(i)
    if a == []:
        a.append(-1)    
    return sorted(a)