def solution(my_string):
    answer = [0] * 52
    for a in my_string:
        if a.isupper():
            b = ord(a) - ord('A')
        else:
            b = ord(a) - ord('a') + 26

        answer[b] += 1
    return answer
    
    # answer = []
    # return answer