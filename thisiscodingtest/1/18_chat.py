def balanced_index(word):
    count = 0
    for index, x in enumerate(word):
        if x == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return index


def is_balanced(word):
    count = 0
    for x in word:
        if x == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
            return count == 0


def solution(word):
    if not word:
        return ""
    index = balanced_index(word)
    u = word[:index + 1]
    v = word[index + 1:]
    if is_balanced(u):
        return u + solution(v)
    else:
        result = "(" + solution(v) + ")"
        u = u[1:-1]
        result += u.replace("(", ")").replace(")", "(")
    return result
