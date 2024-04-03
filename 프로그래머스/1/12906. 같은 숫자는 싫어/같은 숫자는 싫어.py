def solution(arr):
    answer = []
    for i in arr:
        if answer and answer[-1] != i:
            answer.append(i)
            
        elif not answer:
            answer.append(i)
        
            
    return answer