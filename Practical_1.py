#Quick Sort

def quick_sort(arr):
 if len(arr) <= 1:
    return arr
 pivot = arr[len(arr) // 2]
 left = [x for x in arr if x < pivot]
 middle = [x for x in arr if x == pivot]
 right = [x for x in arr if x > pivot]
 return quick_sort(left) + middle + quick_sort(right)
arr = [3, 6, 8, 10, 1, 2, 11]
sorted_arr = quick_sort(arr)
print(sorted_arr)

#Bubble Sort

def bubble_sort(arr):
 n = len(arr)
 for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)

#Sheel Sort

def shell_sort(arr):
 n = len(arr)
 gap = n // 2
 print(f'Value of n: {n}')
 while gap > 0:
    for i in range(gap, n):
        print(f'i: {i}')
 temp = arr[i]
 j = i
 while j >= gap and arr[j - gap] > temp:
    arr[j] = arr[j - gap]
    j -= gap
    arr[j] = temp
    print(gap)
    gap //= 2
arr = [64, 34, 25, 12, 22, 11, 90]
shell_sort(arr)
print(arr)

# Merge Sort

def merge_sort(arr):
 if len(arr) <= 1:
    return arr
 mid = len(arr) // 2
 left = merge_sort(arr[:mid])
 right = merge_sort(arr[mid:])
 return merge(left, right)
def merge(left, right):
 result = []
 i = j = 0
 while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
 result.extend(left[i:])
 result.extend(right[j:])
 return result
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(sorted_arr)

#Selection Sort

def selection_sort(arr):
 n = len(arr)
 for i in range(n):
    min_idx = i
 for j in range(i+1, n):
    if arr[j] < arr[min_idx]:
        min_idx = j
 arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print(arr)