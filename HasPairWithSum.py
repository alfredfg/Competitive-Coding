# Find pair with sum in sorted array
# Eg.1 : [1,2,3,4] Sum=8 : No Pair
# Eg.2 : [1,2,4,4] Sum=8 : Pair Found

# Find pair with sum in unsorted array
# Eg.1 : [1,2,9,4,3,4] Sum=8 : Pair Found
# Eg.2 : [5,2,1,9,2,8] Sum=8 : Not Found

def hasPairWithSumSorted(array, target):
    low = 0
    high = len(array) - 1
    while low < high:
        cur_sum = array[low] + array[high]
        if cur_sum == target:
            return True, (array[low], array[high])
        elif cur_sum < target:
            low += 1
        else:
            high -= 1
    return False, None


def hasPairWithSum(array, target):
    numSet = set()
    for num in array:
        findNum = target - num
        if findNum in numSet:
            return True, (num, target-num)
        else:
            numSet.add(num)
    return False, None


def printResult(isFound, pair):
    if isFound:
        print(pair)
    else:
        print("No pair found")


def testerMethod():
    # Test 1
    isFound, pair = hasPairWithSum([1,6,9,2,6], 8)
    if isFound and pair == (2,6):
        print("Test case 1 passed")
    else:
        print("Test case 1 failed")

    # Test 2
    isFound, pair = hasPairWithSum([1,6,9,4,4], 7)
    if isFound and pair == (6,1):
        print("Test case 2 passed")
    else:
        print("Test case 2 failed")

    # Test 2
    isFound, pair = hasPairWithSum([1,6,9,4,5], 8)
    if isFound is False:
        print("Test case 3 passed")
    else:
        print("Test case 3 failed")


testerMethod()