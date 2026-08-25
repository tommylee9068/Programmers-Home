def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
    if len(answer) > 1:
        return arr[answer[0]:answer[-1]+1]
    elif len(answer) == 1:
        return [arr[answer[0]]]
    else:
        return [-1]