from collections import deque

open = ['(', '[']
close = [')', ']']
stack = deque()
while True:
    stack = deque()
    sentence = input()
    isBreak = False
    if sentence == '.':
        break
    for character in sentence:
        if character in open:
            stack.append(character)
        elif character in close:
            if len(stack) == 0:
                print('no')
                isBreak = True
                break
            pop = stack.pop()
            if pop == '(' and character != ')' or pop == '[' and character != ']':
                print('no')
                isBreak = True
                break

    if len(stack) == 0 and isBreak is False:
        print('yes')
    if isBreak is False and len(stack) != 0:
        print('no')
