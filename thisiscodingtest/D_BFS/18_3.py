def balance(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def correct(w):
    count = 0
    for x in w:
        if x == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(w):
    if w == '':
        return '';
    answer = '';

    index = balance(w)
    u = w[:index + 1]
    v = w[index + 1:]
    if correct(w):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
    answer += ''.join(u)
    return answer


print(solution("()))((()"))
