def solution(my_string, indices):
    a = sorted(indices, reverse = True)
    for i in a:
        if i == 0:
            my_string = my_string[1::]
        elif i > 0:
            my_string = my_string[0:i] + my_string[i+1::]
    return my_string
    
    # answer = ''
    # return answer