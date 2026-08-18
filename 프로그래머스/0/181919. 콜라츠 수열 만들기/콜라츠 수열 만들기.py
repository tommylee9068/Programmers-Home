def solution(n):
    a = [n]
    while n != 1:
        if n % 2 ==0:
            n = n / 2
            a.append(n)
        elif n % 2 != 0:
            n = n * 3 + 1
            a.append(n)
        elif n == 1:
            a.append(1)
            break
    return a
            
    
    # answer = []
    # return answer