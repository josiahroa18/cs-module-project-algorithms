'''
Input: a List of integers
Returns: a List of integers
Time Complexity: O(n)
Space Complexity: O(n)
'''
def moving_zeroes(arr):
    zero_count = 0
    new_arr = []
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            new_arr.append(num)
    for x in range(zero_count):
        new_arr.append(0)
    return new_arr
        
'''
Optimized Solution
Time Complexity: O(n)
Space Complexity: O(1)
'''
def moving_zeroes(arr):
    front = 0
    end = len(arr)-1
    while front is not end:
        if arr[end] == 0:
            end -= 1
            if front is end:
                break
        if arr[front] == 0:
            arr[front], arr[end] = arr[end], arr[front]
        front += 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

