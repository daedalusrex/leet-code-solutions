from typing import List, Tuple


def parent(i: int) -> int:
    return (i - 1) // 2


def heapifyup(nums):
    i = len(nums) - 1
    while i > 0:
        if nums[i] > nums[parent(i)]:
            nums[i], nums[parent(i)] = nums[parent(i)], nums[i]
        i = parent(i)


def left(i):
    return (i * 2) + 1


def right(i):
    return (i * 2) + 2


def heapifydown(nums, node: int):
    # print(f"heapify {nums=}")
    max_i = node
    l = left(node)
    r = right(node)

    if l < len(nums) and nums[max_i] < nums[l]:
        max_i = l
    if r < len(nums) and nums[max_i] < nums[r]:
        max_i = r
    if max_i != node:
        nums[node], nums[max_i] = nums[max_i], nums[node]
        heapifydown(nums, max_i)


class SolutionKthLargest:
    # https://leetcode.com/submissions/detail/1174937427/
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # just make it do the heapify!
        heap = []
        for num in nums:
            heap.append(num)
            heapifyup(heap)
            # print(f"{heap=}")

        pop = 0
        for _ in range(k):
            if len(heap) == 1:
                return heap.pop()
            pop = heap[0]
            heap[0] = heap.pop()
            heapifydown(heap, 0)
            # print(f"post heapify {heap=}")
        return pop


class SolutionCoinChange:
    # https://leetcode.com/submissions/detail/1174905569/
    def coinChangeGreedy(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        count = 0
        for denom in coins:
            while amount >= denom and amount > 0:
                count += 1
                amount -= denom
                print(f"{amount=}, {denom=}, {count=}")

        if amount != 0:
            return -1
        return count

    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP
        coins.sort()

        dp_arr = [0] + ([float("inf")] * amount)
        for i in range(1, amount + 1):
            for denom in coins:
                if denom <= i:
                    previous_min_coins = dp_arr[i - denom]
                    dp_arr[i] = min(previous_min_coins + 1, dp_arr[i])

        print(f"{dp_arr=}")

        if dp_arr[amount] == float("inf"):  # -1 also works
            return -1
        return dp_arr[-1]


class SolutionSubSequence:
    # https://leetcode.com/submissions/detail/1174877428/
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        atleastonematch = False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                if i + 1 == len(s):
                    return True
                i += 1
                j += 1
            elif s[i] != t[j]:
                j += 1

        return False


class SolutionValidParentheses:
    # https://leetcode.com/submissions/detail/1174810910/
    def isValid(self, s: str) -> bool:
        closer = {"}", "]", ")"}
        opener = {"{", "[", "("}
        mapper = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for char in s:
            if char in opener:
                stack.append(char)
            elif char in closer:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if char != mapper.get(prev):
                    return False

        if len(stack) == 0:
            return True
        return False


class SolutionCommonPrefix:
    # https://leetcode.com/submissions/detail/1174799679/
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for word in strs[1:]:
            shared_lcp = ""
            for lcp_char, word_char in zip(lcp, word):
                if lcp_char == word_char:
                    shared_lcp += lcp_char
                else:
                    break
            lcp = shared_lcp

        return lcp


class SolutionNumOfIslands:
    # https://leetcode.com/submissions/detail/1170405742/
    def numIslands(self, grid: List[List[str]]) -> int:
        # print(grid)
        height = len(grid)
        width = len(grid[0])
        print(f"{height=}, {width=}")
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # print(f"{visited}")
        num_islands = 0
        for row, row_array in enumerate(grid):
            for col, value in enumerate(row_array):
                if visited[row][col] == False and value == "1":
                    num_islands += 1
                    self.Dfs_Island(grid, visited, row, col)
                    # print("My Travels")
                    # [print(row) for row in visited]
                visited[row][col] = True

        return num_islands

    def Dfs_Island(self, grid, visited, row, col):
        stack: List[Tuple] = []
        stack.append((row, col))
        while len(stack) != 0:
            (row, col) = stack.pop()
            visited[row][col] = True
            coords = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            # print(f"{coords=}")
            for r, c in coords:
                if (
                    r >= 0
                    and c >= 0
                    and r < len(grid)
                    and c < len(grid[0])
                    and not visited[r][c]
                    and grid[r][c] == "1"
                ):
                    # print(f"Append {r=}, {c=}")
                    stack.append((r, c))


class SolutionLongestConsecutiveSubsequence:
    # https://leetcode.com/submissions/detail/1170395596/
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        largest = 0
        for num in nums:
            if (num - 1) not in all_nums:
                seq = num + 1
                count = 1
                while seq in all_nums:
                    seq += 1
                    count += 1
                largest = max(count, largest)
        return largest
        # max_num = max(nums)
        # min_num = min(nums)
        # if there are duplicates? what is correct answer? (i.e. 1,2,2,3 == 4 or 3? I'd assume 3) -> case 2 confirms
        # walk through array, and build chains?
        #   need all chains because, (one must be longest),
        #   nums not sorted, so can't know if present done or not with others
        #   can't sort , but can get max and min!!!!! in On
        # don't need chains just size, and start pos.
        # (if < start or >start+len -> ++len)  || key -> start, end
        # how to check if belongs in chain?

        # At reach: max/min, set
        # can I combine max/min + walk somehow?

        # start the dumb way, of walk from min to max (which could be toooo huge)
        # dumb way won't work, need the (hash map of chains) + walk !!!!
        # how to set up the key? It's got to be numbers.. -> which is the set itself.
        # So given a hash, what is the O(n) way to check it's longest sequence?
        chains = {}
        largest = 0

        for i in nums:
            # WAIT. Build the set as you go.
            # EVEN BETTER a dict of (Key?) to set()
            # KEY KEY KEY must be int.
            # int -> set()
            # Sets are mutable and shared in memory -> BOOM
            # Keys also work for detection
            if i not in chains.keys():
                # print(f"before: {i=}")
                if (i + 1 in chains.keys()) and (i - 1 in chains.keys()):
                    # problem. need to modify the sets in place, because other mems point at them
                    joined = chains[i + 1] | chains[i - 1] | {i}
                    # chains[i-1].update(joined)  # seems to not be in right place of memory
                    # chains[i+1].update(joined)
                    # chains[i] = joined
                    # is this technically not order N?
                    for j in joined:
                        chains[j] = joined
                elif i + 1 in chains.keys():
                    chains[i + 1].add(i)
                    chains[i] = chains[i + 1]
                elif i - 1 in chains.keys():
                    chains[i - 1].add(i)
                    chains[i] = chains[i - 1]
                else:
                    chains[i] = {i}

                if len(chains[i]) > largest:
                    largest = len(chains[i])
            # print(f"after: {i=}  {chains=}")
        return largest
        # there is a fance way to get max size of all these


class Solution:
    # https://leetcode.com/submissions/detail/1163532983/
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k_mod = k % len(nums)
        index = len(nums) - k_mod
        # new_array = nums[:] # deep copy?
        # nums[:] = new_array[index:]
        # nums[len(nums):] = new_array[:len(nums) - k_mod]
        # Haha, Fancy python list expansion
        nums[:] = [*nums[index:], *nums[:index]]
        # for i in range(len(nums)):

        #     nums[i] = nums[index]
        #     index += 1

        return None
