'''
THUẬT TOÁN TÌM KIẾM
'''

#? Tìm kiếm tuyến tính (Linear Search)

'''
    @params: input_arr, target
    - input_arr: mảng cần duyệt
    - target: giá trị mình muốn tìm kiếm
'''
def linear_search(input_arr, target):
    for item in input_arr:
        if item == target:
            return item
        else:
            return -1
        

        
#? Tìm kiếm nhị phân (Binary Search)

'''
    @params: input_arr, target
    - input_arr: mảng cần duyệt
    - target: giá trị mình muốn tìm kiếm
    
    @note: dừng vòng lặp khi head > tail
'''
def binary_search(input_arr, target):
    # 1. Sắp xếp lại mảng (k nằm trong thuật toán)
    input_arr.sort()
    
    # 2. Xác định vị trí index đầu và index cuối
    head = 0
    tail = len(input_arr) - 1 # 4
    
    # 3. Tính vị trí chính giữa 
    middle = (head + tail) // 2 
    
    # 4. Kiểm tra giá trị tại index chính giữa
    while head <= tail:
        if input_arr[middle] == target:
            return 1
        else:
            # 5. Cập nhật head hoặc tail nếu không tìm được target
            if input_arr[middle] > target:
                tail = middle - 1
            else:
                head = middle + 1
                
            middle = (head + tail) // 2
    
    return -1

numbers = [1, 10, 7, 30, 22, 25, 120, 15, 18, 19]
target = int(input("Nhập số để tìm kiếm: "))

# result = linear_search(numbers, target)
result = binary_search(numbers, target)

if result == 1:
    print(f"Tìm thấy số: {target}")
else:
    print(f"Không tìm thấy số: {target}")
    
