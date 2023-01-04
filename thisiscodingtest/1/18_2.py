def balance(word):
    count = 0
    for i in range(len(word)):
        if word[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def correct(word):
    count = 0
    for i in range(len(word)):
        if word[i] == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return True


def solution(word):
    answer = ''
    if word == '':
        return ''

    index = balance(word)
    u = word[:index + 1]
    v = word[index + 1:]

    if correct(word):
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
        print(answer)
    return answer


# data = "(()())()"
print(solution(")("))
# (()())()
# (()())()
