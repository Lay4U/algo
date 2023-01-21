from typing import List


def find_index(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1


n = int(input())
array = list(map(int, input().split()))

index = find_index(array)
print(index)
