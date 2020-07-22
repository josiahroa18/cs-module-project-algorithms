'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Time Complexity: O(n + n + n) = O(3n) = O(n)
    # Space Complexity: O(n)
    # Go through the list once and store all values into a hash table
    # Go through the list again and count how many times each value appears
    # If a value only appears once, return that value
    found = {}
    for num in arr: #O(n)
        if num not in found.keys(): #O(1)
            found[num] = 0 #O(1)
    for num in arr: #O(n)
        found[num] += 1 #O(1)
    for num, count in found.items(): #O(n)
        if count == 1: #O(1)
            return num

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# Can Impvrove on this by sorting the list to bring space complexity to O(1)