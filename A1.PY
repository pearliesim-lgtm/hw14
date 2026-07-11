def find_one_odd(nums):
    xor_sum=0
    for num in nums:
        xor_sum^=num
    return xor_sum
def find_two_odd(nums):
    xor_sum=0
    for num in nums:
        xor_sum^=num
    bit=xor_sum & -xor_sum
    x,y=0,0
    for num in nums:
        if num&bit:
            x^=num
        else:
            y^=num
    return[x,y]
list_one=[2,3,5,4,5,2,4,3,5]
print("One odd number:",find_one_odd(list_one))
list_two=[2,3,7,4,3,2,4,5]
print("Two odd numbers:",find_two_odd(list_two))  