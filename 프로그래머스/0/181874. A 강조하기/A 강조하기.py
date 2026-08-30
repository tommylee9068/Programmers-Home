def solution(myString):
    answer = ""
    for i in myString:
        if i == "a":
            i = i.upper()
            answer += i
        elif i == "A":
            answer += i
        elif i.isupper():
            i = i.lower()
            answer += i
        else:
            answer += i
    return answer
    
    # answer = ''
    # return answer