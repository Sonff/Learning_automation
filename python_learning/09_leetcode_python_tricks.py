# =====================================================================
# TOPIC 9: WRITING PYTHON CODE FOR LEETCODE (DSA)
# =====================================================================
# LeetCode ya competitive programming me Python use karne ke standard 
# patterns, built-in helper libraries, aur writing practices.

from typing import List, Optional, Dict

# ---------------------------------------------------------------------
# 1. Understanding LeetCode Class Structure
# ---------------------------------------------------------------------
# LeetCode aapko input read (`input()`) ya print (`print()`) karne ko nahi kehta.
# Woh aapse Class ke andar ek specific function implement karne ko kehta hai.

class ListNode:
    """Standard LeetCode Linked List node definition"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # `self` use karna padta hai class functions ko coordinate karne ke liye.
    # Type hints (jaise `List[int]`) input aur output formats clarify karte hain.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two Sum Solution (Hash Map Pattern)
        """
        seen: Dict[int, int] = {}
        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], index]
            seen[num] = index
        return [] # Default fallback

    # Helper method call karna class ke andar:
    def solveComplexProblem(self, data: List[int]) -> bool:
        # Apne hi class ke doosre method ko call karne ke liye `self.` use karein:
        indices = self.twoSum(data, 10)
        return len(indices) > 0


# ---------------------------------------------------------------------
# 2. Key Libraries for DSA in Python
# ---------------------------------------------------------------------
# Python me competitive programming ke liye 4 main standard tools seekhna zaroori hai.

# A. Collections (deque, Counter, defaultdict)
from collections import deque, Counter, defaultdict

print("--- A. Collections Demo ---")
# 1. deque: BFS ya sliding queue ke liye O(1) append/pop left aur right dono se.
queue = deque([1, 2, 3])
queue.append(4)       # Add to right
queue.appendleft(0)   # Add to left (fast, normal list me list.insert(0) O(N) leta hai)
print(f"Deque: {queue}")
queue.popleft()       # Removes 0
print(f"After popleft: {queue}")

# 2. Counter: Frequency count karne ke liye (Anagrams or character counting problems)
word = "automation"
freq = Counter(word)
print(f"Char Frequencies: {freq}")
print(f"Top 2 common chars: {freq.most_common(2)}")

# 3. defaultdict: Agar key check nahi karni ho aur direct append/increment karna ho
adj_list = defaultdict(list) # Default value empty list [] hogi
adj_list["nodeA"].append("nodeB") # No KeyError raised!
print(f"Graph representation: {adj_list}\n")


# B. Heaps (heapq)
# Priority Queue (Min-Heap by default)
import heapq

print("--- B. Heaps Demo ---")
heap = []
# Elements push karna
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

# Sabse chota element O(1) me top pe hota hai aur O(log N) me pop hota hai
smallest = heapq.heappop(heap)
print(f"Smallest element popped: {smallest} (Remaining: {heap})")

# Max-Heap hack: Negative numbers insert karke pop ke waqt multiply by -1 karein:
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -20)
print(f"Max element: {-1 * heapq.heappop(max_heap)}\n")


# C. Binary Search (bisect)
import bisect

print("--- C. Binary Search Demo ---")
arr = [1, 3, 4, 4, 6, 8]
# 4 insert karne ki left-most index kya hogi to maintain sorted order?
idx_left = bisect.bisect_left(arr, 4)
# 4 insert karne ki right-most index kya hogi?
idx_right = bisect.bisect_right(arr, 4)
print(f"Bisect Left: {idx_left} (index 2)")
print(f"Bisect Right: {idx_right} (index 4)\n")


# ---------------------------------------------------------------------
# 3. Python LeetCode Best Practices / Hacks
# ---------------------------------------------------------------------
# 1. Float Infinity: Min/Max variables initialized karne ke liye:
max_val = float('-inf') # Lowest possible value
min_val = float('inf')  # Highest possible value

# 2. Swap in 1 line:
a, b = 5, 10
a, b = b, a # Python internal tuple unpacking se swap karta hai, temp variable ki zaroori nahi.

# 3. Divmod: Division aur Remainder ek sath nikalna:
quotient, remainder = divmod(17, 5) # (3, 2)

# 4. Sorting with custom keys (multi-level sorting):
# Sort by age (ascending), but if age matches, sort by name (alphabetically)
candidates = [("Alice", 25), ("Bob", 20), ("Alex", 20)]
candidates.sort(key=lambda x: (x[1], x[0]))
print(f"Multi-key Sorted Candidates: {candidates}")
print()


# ---------------------------------------------------------------------
# 4. Mock execution of Leetcode Solution
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Local terminal me output test karne ke liye Solution instantiate karein:
    sol = Solution()
    
    # Test case 1: Two Sum
    nums_input = [2, 7, 11, 15]
    target_val = 9
    result = sol.twoSum(nums_input, target_val)
    print(f"LeetCode Style Test Result (Two Sum): {result}")
