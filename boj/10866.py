N = int(input())
data = []
for _ in range(N):
    data.append(input())
# data = [r for r in data if r]

deck = []
for q in data:
    if 'push_back' in q:
        deck.append(q.split()[1])
    elif 'push_front' in q:
        deck.insert(0, q.split()[1])
    elif 'pop_front' == q:
        print(deck.pop(0) if deck else -1)
    elif 'pop_back' == q:
        print(deck.pop() if deck else -1)
    elif 'size' == q:
        print(len(deck))
    elif 'empty' == q:
        print(0 if deck else 1)
    elif 'front' == q:
        print(deck[0] if deck else -1)
    elif 'back' == q:
        print(deck[-1] if deck else -1)
