def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


arr = [2,21,12,1]

bubblesort(arr)
print(arr)