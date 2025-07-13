"""
return the count and list of odd numbers in the given range (low,high)
"""


def oddNum(low, high):
    if low < 0:
        return 0, "Error! Negative integers are not allowed."
    elif low > high:
        return 0, "Error! Low cannot be greater than High."
    elif low % 2 == 0:
        low += 1
    elif high % 2 == 0:
        high -= 1
    count = (high-low)//2+1
    numList = [x for x in range(low, high+1, 2)]
    statement = f"The odd numbers between {low} and {high} are {numList}."
    return count, statement


a = int(input("Enter low integer: "))
b = int(input("Enter high integer: "))
count, statement = oddNum(a, b)
print(f"Count: {count}")
print(f"Conclusion: {statement}")
