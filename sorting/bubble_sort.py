def bubble_sort(nums):
    lens = len(nums)

    for i in range(lens):
        for j in range(0, lens - i - 1):
            if int(nums[j]) > int(nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


data = input('Enter numbers separated by spaces: ')
sorted_data = bubble_sort(data.split())

print('nums: ', sorted_data)

####################################################

nums1 = [1, 2, 3, 3, 2, 1]
length = len(nums1)
for i in range(length):
    for j in range(0, length - i - 1):
        if nums1[j] > nums1[j + 1]:
            tmp = nums1[j]
            nums1[j] = nums1[j + 1]
            nums1[j + 1] = tmp

print(nums1)
