def solution(a, b):
    A = str(a)
    B = str(b)
    
    if int(A+B) >= int(B+A):
        answer = int(A+B)
                    
        
    else:
        answer = int(B+A)
    
    return answer