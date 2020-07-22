'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # passes in an array of numbers with one odd number thats not like the others
    # If the array length is less than 1 return the array
    # Loop through and compare the current index with the next untill
    numbers = []
    for i in arr:
        # if the number is in the array pass
        if i in numbers:
            pass
        # once all the numbers are in there if the count of an item is one its the odd number out
        if arr.count(i) == 1:
            return i
        # then if the number is not in the list append it
        else:
            numbers.append(i)

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")