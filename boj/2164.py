n = int(input())
n = [i for i in range(1, n + 1)]
while len(n) > 1:
    deque = n
    deque.pop(0)
    deque.append(deque.pop(0))

print(*n)
from collections import deque

n = int(input())
cards = deque(range(1, n + 1))
while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)
print(*cards)

'''
제시해주신 코드와 제가 제시한 코드의 차이점은 deque의 사용 여부입니다. deque는 양쪽 끝에서 삽입과 삭제가 가능한 자료구조로, list에 비해 이러한 연산이 훨씬 빠릅니다.

제시해주신 코드에서는 list를 사용하여 pop(0) 연산을 수행하는데, 이는 list의 첫 번째 요소를 제거하고 나머지 요소들을 한 칸씩 앞으로 이동시키는 작업이므로 시간 복잡도가 O(n)입니다. 따라서 전체 시간 복잡도는 O(n^2)가 됩니다.

반면에 제가 제시한 코드에서는 deque를 사용하여 popleft() 연산을 수행하는데, 이는 deque의 첫 번째 요소를 제거하는 작업으로 시간 복잡도가 O(1)입니다. 따라서 전체 시간 복잡도는 O(n)이 됩니다.

rotate() 함수는 deque의 요소들을 회전시키는 함수입니다. 인자로 정수 n을 전달하면, 양수인 경우 오른쪽으로 n번 회전하고, 음수인 경우 왼쪽으로 n번 회전합니다. 예를 들어, deque([1, 2, 3, 4]).rotate(-1)은 [2, 3, 4, 1]이 됩니다.
'''
