def balanced_index(word):
    count = 0
    for index, x in enumerate(word):
        if x == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return index


def property_word(word):
    count = 0
    for x in word:
        if x == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(word):
    answer = ''
    if word == '':
        return answer
    index = balanced_index(word)
    u = word[: index + 1]
    v = word[index + 1:]
    if property_word(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for index, x in enumerate(u):
            if x == '(':
                u[index] = ')'
            else:
                u[index] = ')'
        answer += ''.join(u)
    return answer
