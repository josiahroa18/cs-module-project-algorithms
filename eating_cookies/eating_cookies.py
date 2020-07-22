'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    
    count = 0
    count += eating_cookies(n - 1)
    count += eating_cookies(n - 2)
    count += eating_cookies(n - 3)

    return count

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
