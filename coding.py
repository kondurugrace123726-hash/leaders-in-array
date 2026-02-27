
"""Input:
n = size of array
arr = list of integers """

from typing import List

def find_leaders(arr: List[int]) -> List[int]:
    # Return all leaders in the array.
    if not arr:
        return []

    max_right = arr[-1]
    leaders = [max_right]

    # Traverse from right to left
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]

    leaders.reverse()
    return leaders


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))

    result = find_leaders(arr)

    if result:
        print(*result)
    else:
        print(-1)