def solution(n, k):
    number = n//10
    if n>=10:
        answer = (n*12000) + ((k-number)*2000)
    else:
        answer = (n*12000) + (k*2000)
    return answer