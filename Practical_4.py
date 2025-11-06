#Radix Sort

def radix_sort(arr):
 exp = 1
 max_num = max(arr)
 while max_num // exp > 0:
    count = [0] * 10
    output = [0] * len(arr)
 for num in arr:
    count[(num // exp) % 10] += 1
 for i in range(1, 10):
    count[i] += count[i - 1]
 for num in reversed(arr):
    digit = (num // exp) % 10
 output[count[digit] - 1] = num
 count[digit] -= 1
 arr[:] = output
 exp *= 10
numbers = [20, 2, 7, 15, 1, 6, 8]
radix_sort(numbers)
print(f'\n{numbers}\n')

#Counting Sort

def counting_sort(arr):
 max_val = max(arr)
 min_val = min(arr)
 range_of_elements = max_val - min_val + 1
 count = [0] * range_of_elements
 output = [0] * len(arr)
 for num in arr:
    count[num - min_val] += 1
 for i in range(1, range_of_elements):
    count[i] += count[i - 1]
 for num in reversed(arr):
    output[count[num - min_val] - 1] = num
    count[num - min_val] -= 1
 for i in range(len(arr)):
    arr[i] = output[i]
numbers = [20, 2, 7, 15, 1, 6, 8]
counting_sort(numbers)
print(f'\n{numbers}\n')

#Bucket Sort

def bucket_sort(arr):
 n = len(arr)
 if n == 0:
    return
 buckets = [[] for _ in range(n)]
 min_val, max_val = min(arr), max(arr)
 range_val = (max_val - min_val) / n
 for num in arr:
    index = int((num - min_val) / range_val)
    if index == n:
        index -= 1
    buckets[index].append(num)
 arr.clear()
 for bucket in buckets:
    bucket.sort()
    arr.extend(bucket)
numbers = [0.20, 0.2, 0.7, 0.15, 0.1, 0.6, 0.8]
bucket_sort(numbers)
print(f'\n{numbers}\n')
