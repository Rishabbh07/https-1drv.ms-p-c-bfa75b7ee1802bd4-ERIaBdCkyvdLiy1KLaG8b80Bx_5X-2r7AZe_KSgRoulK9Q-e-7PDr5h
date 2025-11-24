def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


my_list = [64, 34, 25, 12]
bubble_sort(my_list)
print(my_list) 




# Using .sort() (Modifies original)
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]

# Using sorted() (Creates new list)
data = [10, 3, 7]
new_data = sorted(data)
print(new_data) # Output: [3, 7, 10]
print(data)     # Output: [10, 3, 7]






