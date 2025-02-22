'''
Bubble Sort (sắp xếp nổi bọt)
'''

def bubble_sort(arr):
    
    n = len(arr)
    
    for i in range(n): # 0 -> n - 1
        for j in range(0, n - 1 - i): # 0 -> n - 1 - i
            if arr[j] > arr[j+1]:
                # Đổi chỗ giá trị tại 2 vị trí index
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                #? 1 cách làm khác cho việc đổi chỗ -> đặt biến tạm
                # temp = arr[j]
                # arr[j] = arr[j + 1]
                # arr[j + 1] = temp
                

