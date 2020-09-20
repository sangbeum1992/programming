par1 = ["leo","kiki","eden"]
com1 = ["eden","kiki"]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part
        print(dic[hash(part)])
        temp += int(hash(part))
        print(temp)

    for com in completion:
        dic[hash(com)] = com
        print(com)
        temp -= int(hash(com))
        print(temp)

    answer = dic[temp]

    return answer

solution(par1, com1)
        
