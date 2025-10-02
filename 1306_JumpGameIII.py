from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        visits: set = set()
        queue = deque()
        visits.add(start)
        queue.append(start)

        n = len(arr)
        while queue:
            curr = queue.pop()
            right = curr + arr[curr]
            left = curr - arr[curr]
            if right < n and right not in visits:
                if arr[right] == 0:
                    return True

                visits.add(right)
                queue.append(right)

            if left >= 0 and left not in visits:
                if arr[left] == 0:
                    return True

                visits.add(left)
                queue.append(left)

        return False