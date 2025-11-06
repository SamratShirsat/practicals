import heapq
def kthSmallest(arr, K):
 max_heap = []
 for num in arr:
    heapq.heappush(max_heap, -num)
 if len(max_heap) > K:
    heapq.heappop(max_heap)
 return -max_heap[0]
def kthLargest(arr, K):
 min_heap = []
 for num in arr:
    heapq.heappush(min_heap, num)
 if len(min_heap) > K:
    heapq.heappop(min_heap)
 return min_heap[0]
if __name__ == "__main__":
 arr = [2, 6, 3, 1, 21, 25, 8, 13, 69, 5]
 K = 4
 print(f"Array: {arr}")
 print(f"K = {K}")
 print(f"Kth smallest element: {kthSmallest(arr, K)}")
 print(f"Kth largest element: {kthLargest(arr, K)}")

 # Median of Median

def median_of_medians(arr, k):
 sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]

 medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

 # Find the median of the medians recursively
 if len(medians) <= 5:
    pivot = sorted(medians)[len(medians)//2]
 else:
    pivot = median_of_medians(medians, len(medians)//2)

 # Partition the array around the pivot
 low = [el for el in arr if el < pivot]
 high = [el for el in arr if el > pivot]
 pivots = [el for el in arr if el == pivot]

 # Select the kth element
 if k < len(low):
    return median_of_medians(low, k)
 elif k < len(low) + len(pivots):
    return pivot
 else:
    return median_of_medians(high, k - len(low) - len(pivots))
arr = [2, 6, 3, 1, 21, 25, 8, 13, 69, 5]
k = len(arr) // 2
median_value = median_of_medians(arr, k)
print(f"The {k}th smallest element is: {median_value}")
