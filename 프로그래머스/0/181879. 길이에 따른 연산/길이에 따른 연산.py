def solution(num_list):
    
    if len(num_list) >= 11:
        a = 0
        for i in range(len(num_list)):
            a += num_list[i]
        return a
    elif len(num_list) <= 10:
        b = 1
        for i in range(len(num_list)):
            b = b * num_list[i]
        return b
    
    # answer = 0
    # return answer