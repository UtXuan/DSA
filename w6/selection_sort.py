'''
Selection Sort (sắp xếp chọn)
'''

def selection_sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Đổi chỗ giá trị tại 2 vị trí index
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        #? 1 cách làm khác cho việc đổi chỗ
        # temp = arr[i]
        # arr[i] = arr[min_index]
        # arr[min_index] = temp