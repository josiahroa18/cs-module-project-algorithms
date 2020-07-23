'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
# Time Complexity: O(n + n + n) = O(3n) = O(n)
# Space Complexity: O(n)
'''
def single_number(arr):
    found = {}
    for num in arr: #O(n)
        if num not in found.keys(): #O(1)
            found[num] = 0 #O(1)
    for num in arr: #O(n)
        found[num] += 1 #O(1)
    for num, count in found.items(): #O(n)
        if count == 1: #O(1)
            return num

'''
Optimized Solution
Time Complexity: O(n)
Space Complexity: O(1)
'''
# def single_number(arr):
#     for i in range(1, len(arr)):
#         # If match, arr[0] = 0, if no match, arr[0] = arr[i]
#         arr[0] ^= arr[i]
#     return arr[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
