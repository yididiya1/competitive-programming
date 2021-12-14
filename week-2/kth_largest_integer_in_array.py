def kthLargestNumber(nums, k):
        
        int_nums = list(map(int,nums))
        
        int_nums.sort()
       
#         for i in range(1,len(int_nums)):
#             key = int_nums[i]
#             j = i - 1
#             while j >= 0 and key < int_nums[j]:
#                 int_nums[j+1] = int_nums[j]
#                 j -= 1           
#             int_nums[j+1] = key
    
#         for i in range(len(int_nums)):
#             for j in range(0,len(int_nums)-i-1):
#                 if int_nums[j] > int_nums[j+1]:
#                     int_nums[j], int_nums[j+1] = int_nums[j+1], int_nums[j]
          

        return str(int_nums[len(nums)-k])

example = kthLargestNumber(["2","21","12","1"],3)
print(example)
        